from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from account.models import User



# user camelCase for class names
class OurUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'password1', 'password2','role', 'username']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['profile_picture', 'phone_number', 'email', 'username', 'first_name', 'last_name']
