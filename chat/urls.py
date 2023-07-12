from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('users/add', views.UserCreate.as_view()),
    path('chats/', views.ChatList.as_view()),
    path('chats/add', views.ChatCreate.as_view()),
    path('messages/', views.MessageList.as_view()),
    path('messages/add', views.MessageCreate.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
