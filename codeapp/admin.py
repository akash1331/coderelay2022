from django.contrib import admin
from codeapp.models import *
# Register your models here.

admin.site.site_header = 'CodeRelay Admin'

class itemdataAdminSite(admin.ModelAdmin):
    list_display = ['Name','type','Owner','dateuploaded','Desc','cost']

class itemtypeAdminSite(admin.ModelAdmin):
    list_display = ['types_of_item']

admin.site.register(itemstype,itemtypeAdminSite)
admin.site.register(itemdata,itemdataAdminSite)