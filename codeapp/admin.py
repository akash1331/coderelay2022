from django.contrib import admin
from codeapp.models import *
# Register your models here.

admin.site.site_header = 'CodeRelay Admin'

admin.site.register(itemstype)
admin.site.register(itemdata)