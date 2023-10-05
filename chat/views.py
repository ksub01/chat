<<<<<<< HEAD
from rest_framework import generics
from . import serializers
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer 


class UserCreate(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer


class ChatList(generics.ListAPIView):

    def get_queryset(self):
        user = self.request.query_params.get('user')
        return Chat.objects.filter(users=user).order_by('created_at')

    serializer_class = serializers.ChatSerializer


class ChatCreate(generics.CreateAPIView):
    serializer_class = serializers.ChatSerializer


class MessageList(generics.ListAPIView):

    def get_queryset(self):
        chat = self.request.query_params.get('chat_id')
        return Message.objects.filter(chat_id=chat).order_by('-created_at')

    serializer_class = serializers.MessageSerializer


class MessageCreate(generics.CreateAPIView):
    serializer_class = serializers.MessageSerializer
=======
from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema
from .serializers import MessageSerializer, ChatSerializer
from .permissions import *
from rest_framework.authentication import * 
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from django.views.decorators.csrf import csrf_exempt
from .models import Message, Chat
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)



class MessageViewSet(viewsets.ModelViewSet):

    queryset = Message.objects.all()
    serializer_class = MessageSerializer 



class ChatViewSet(viewsets.ModelViewSet):

    queryset = Chat.objects.all()
    serializer_class = ChatSerializer 

>>>>>>> origin/main
