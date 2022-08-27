from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('chats/', views.ChatSessionView.as_view()),#to activate a chatroom
    path('chats/<uri>/', views.ChatSessionView.as_view()),#to join exesting chatroom
    path('chats/<uri>/messages/', views.ChatSessionMessageView.as_view()),#to share messages
]