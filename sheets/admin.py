from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(CustomUser, admin.ModelAdmin)
admin.site.register(Sheet, admin.ModelAdmin)
