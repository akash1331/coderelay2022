from django.db import models
from django.db.models.deletion import SET_NULL
from django.db.models.fields.files import ImageField
from authentications.models import *

# Create your models here.
class itemstype(models.Model):
    types_of_item = models.CharField(max_length=50)

class itemdata(models.Model):
    Name = models.CharField(("Name"), max_length=15)
    type =models.ForeignKey(itemstype,on_delete=SET_NULL,null=True)
    Owner = models.TextField(("Owner"))
    dateuploaded = models.DateTimeField(("Date uploaded"), auto_now=False, auto_now_add=True)
    Desc =  models.TextField(("Description"))
    cost = models.IntegerField(("Cost"))
    image =models.ImageField(("Image"), upload_to="Images", height_field=None, width_field=None, max_length=None)