from django.contrib import admin

from .models import *

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')


admin.site.register(CustomUser, CustomUserAdmin)
