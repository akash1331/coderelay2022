from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register(UserAccount)
# # Register your models here.

@admin.register(UserAccount)
class postadmin(admin.ModelAdmin):
    class Meta:
        model = UserAccount