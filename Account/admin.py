from django.contrib import admin

from account.views import register
from . models import User
# Register your models here.
admin.site.register(User)