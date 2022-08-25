
from django.db import models
from django.contrib.auth import authenticate
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, full_name, email, phone_number, password=None):
        if not full_name:
            raise ValueError("Users must have full name")
        if not email:
            raise ValueError("Users must have email")
        if not phone_number:
            raise ValueError("Users must have phone number")
        
        user=self.model(
            full_name=full_name,
            email=self.normalize_email(email),
            phone_number=phone_number,
        )
        
        user.set_password(password)
        user.is_active=True
        user.save(using=self._db)
        return user
    
    def create_superuser(self, full_name, email, phone_number, password):
        user=self.create_user(
            full_name=full_name,
            email=self.normalize_email(email),
            phone_number=phone_number,
            password=password,
        )
        
 
        user.is_staff = True
        user.is_admin=True
        user.is_superuser=True
        user.save(using=self._db)
        return user
    
    
    
class User(AbstractBaseUser):
    full_name=models.CharField(max_length=255, null=True)
    email=models.EmailField(max_length=200, unique=True, null=True)
    phone_number=PhoneNumberField(unique=True, null=True)
    last_login=models.DateTimeField(auto_now=True)
    date_joined=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    is_routeadmin=models.BooleanField(default=False)
    is_busadmin=models.BooleanField(default=False)

    # updated=models.DateTimeField(auto_now=True)
    # created=models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD='phone_number'
    REQUIRED_FIELDS=['full_name', 'email']
    
    objects=MyUserManager()
    
    def __str__(self):
        return self.full_name
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    # @property
    # def is_staff(self):
 
    #     return self.staff

    # @property
    # def is_admin(self):
       
    #     return self.admin
    
    @property
    def active(self):
       
        return self.is_active
    

    
    
    
    