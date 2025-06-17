from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, School

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'user_type', 'student_id', 'is_active', 'date_joined')
    list_filter = ('user_type', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        (('Additional Info'), {'fields': ('user_type', 'phone_number', 'date_of_birth', 'profile_picture', 'student_id')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (('Additional Info'), {'fields': ('user_type', 'phone_number', 'date_of_birth', 'profile_picture', 'student_id')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(School)