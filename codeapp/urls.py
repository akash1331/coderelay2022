"""codeapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from codeapp.views import *

urlpatterns = [
    path('dataapi/', dataApi.as_view(), name='dataapi'),
    path('dataapi/<int:id>', datadetail.as_view(), name='dataapii'),
    path('typeapi/', typeApi.as_view(), name='typeapi'),
    path('filter/', typefilter.as_view(), name='filter'),
    # path('search/<str:id>', searchApi.as_view(), name='filter'),
    path('searchdata/', searchdata.as_view(), name='searchdata'),
    path('searchtype/', searchtype.as_view(), name='searchtype'),

]
