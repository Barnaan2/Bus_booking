from django.db import models
from django.contrib.auth.models import AbstractUser
# from django_softdelete.models import SoftDeleteModel


class User(AbstractUser):
    phone_number = models.CharField(max_length=20, unique=True)
    role = models.CharField(max_length=20)
    profile_picture = models.ImageField(null=True, default="avatar.png")
    # USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []