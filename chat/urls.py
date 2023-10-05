<<<<<<< HEAD
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
=======
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

>>>>>>> origin/main
