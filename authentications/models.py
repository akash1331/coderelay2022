from django.db import models
from django.db.models.signals import pre_save
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import datetime
import random
from django.contrib.auth import logout
from django.shortcuts import redirect
from codeapp.models import *

def unique_usernumber(instance, new_id=None):
    ct = datetime.datetime.now().date()
    number = 1
    if new_id is not None:
        id = new_id
    else:
        id = 'f' + str(ct) +str(number)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(user_id=id).exists()
    if qs_exists:
        new_id = "f{date}{idgen}{rand}".format(
            
            date=ct,
            idgen = number+1,
            rand = random.randrange(0, 100000),
        )
        return unique_usernumber(instance, new_id=new_id)
    
    return id


class UserAccountManager(BaseUserManager):

    def create_superuser (self, email,password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        if other_fields.get('is_staff') is not True:
             raise ValueError(
                 "Superuser must be assigned to is_staff=True.")
        if other_fields.get('is_superuser') is not True:
             raise ValueError(
                 'Superuser must be assigned to is superuser=True.')
        return self.create_user(email,password, **other_fields)



    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.is_superuser = True
        user.save()

        return user
  
ACCOUNT_TYPEE = (
    ("STUDENT", "student"),
    ("ADMIN", "ADMIN"),
)


class UserAccount(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(null=True,blank=True,max_length=50)
    username = models.CharField(unique=True,null=True,blank=True,max_length=50)
    contact_no = models.BigIntegerField(null=True,blank=True)
    email = models.CharField(primary_key=True,max_length=50)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    type_of_account = models.CharField(
        max_length = 20,
        choices = ACCOUNT_TYPEE,
        default = 'STUDENT'
        )
    objects = UserAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name','contact_no','email']

    def get_name(self):
        return str(self.name)

    def get_username(self):
        return str(self.name)

    def __str__(self):
        return str(self.email)


# def user_number_generator(sender,instance,*args,**kwargs):
#     if  instance.user_id:
#         instance.user_id = unique_usernumber(instance)
# pre_save.connect(user_number_generator,sender=UserAccount)

