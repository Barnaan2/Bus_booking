from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm, UserRegisterForm

User = get_user_model()

# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)
class UserAdmin(UserAdmin):

    form = UserAdminChangeForm
    add_form = UserRegisterForm

    list_display = ['full_name', 'email', 'phone_number','is_admin', 'is_superuser']
    list_filter = ['is_admin']
    fieldsets = (
        (None, {'fields': ('full_name', 'phone_number', 'email', 'password')}),
        # ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('is_admin', 'is_routeadmin', 'is_busadmin', 'is_superuser')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('full_name', 'phone_number','email', 'password1', 'password2')}
        ),
    )
    search_fields = ['email', 'full_name']
    ordering = ['full_name']
    filter_horizontal = ()


admin.site.register(User, UserAdmin)