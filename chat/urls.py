from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token 
from . import views


router = routers.DefaultRouter()
router.register(r'messages', views.MessageViewSet, basename="messages")
router.register(r'chats', views.ChatViewSet, basename="chats")





urlpatterns = [
    path('api-token-auth/', obtain_auth_token),
    path('', include(router.urls)),

        ]

