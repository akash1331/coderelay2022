from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('chats/', views.ChatSessionView.as_view()),#to activate a chatroom   (send post request with username and pw)
    path('chats/<uri>/', views.ChatSessionView.as_view()),#to join existing chatroom   ---- patch request with username
    path('chats/<uri>/messages/', views.ChatSessionMessageView.as_view()),#to share messages
]