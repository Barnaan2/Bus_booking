
from cProfile import label
from django import forms
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.forms import ReadOnlyPasswordHashField

User = get_user_model()



class UserRegisterForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['full_name', 'email', 'phone_number']

#check if email taken
    def clean_email(self):

        email = self.cleaned_data.get('email')
        usr = User.objects.filter(email=email)
        if usr.exists():
            raise forms.ValidationError("Sorry! Email was taken")
        return email
    
    #check if phone_number taken
    def clean_phone_number(self):
    
        phone_number = self.cleaned_data.get('phone_number')
        usr = User.objects.filter(phone_number=phone_number)
        if usr.exists():
            raise forms.ValidationError("Sorry! Phone number was taken")
        return phone_number

    def clean(self):
  
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
       
        if password1 is not None and password1 != password2:
            self.add_error("password2", "Your passwords must match")
        return cleaned_data
    def save(self, commit=True):
         
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active=True
        if commit:
            user.save()
        return user

  #creating new user
class UserAdminCreationForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['full_name', 'email', 'phone_number', 'password']

    def clean(self):

        cleaned_data = super().clean()
        password1 = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")
        if password1 is not None and password1 != password2:
            self.add_error("password2", "Your passwords must match")
        return cleaned_data

    #hash password
    def save(self, commit=True):
     
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    #A form for updating users.
class UserAdminChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ['full_name', 'email', 'phone_number', 'password', 'is_active', 'is_admin']

    def clean_password(self):

        return self.initial["password"]
