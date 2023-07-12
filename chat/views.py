from rest_framework import generics
from . import serializers
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response


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
