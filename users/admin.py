from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
   add_form = CustomUserCreationForm
   form = CustomUserChangeForm
   model = CustomUser
   list_display = ['username','email','is_customer','is_FinancialAdvisor','is_superuser']
   fieldsets = ((None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name','last_name','email')}),
        ('Permissions', {'fields': ('is_customer','is_staff', 'is_active','is_FinancialAdvisor', )}),)

admin.site.register(CustomUser, CustomUserAdmin)
