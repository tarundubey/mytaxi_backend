from django import forms
from django.conf import settings
from django.contrib import admin, messages
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.utils.text import slugify
from django.utils.translation import ugettext as _
from taxi_auth.models import User
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import Group, Permission
#Import your models below
from taxi_auth.models import Role

class MTUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User


class MTUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class PBUserAdmin(UserAdmin):
    form = MTUserChangeForm
    add_form = MTUserCreationForm

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','first_name','last_name','email','password1', 'password2')}
         ),
    )

    list_display = ('username', 'email','mobile','first_name', 'last_name', 'is_staff', 'last_login')

admin.site.register(User, PBUserAdmin)