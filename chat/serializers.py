from rest_framework import serializers
<<<<<<< HEAD
from django.contrib.auth.models import User
from chat.models import *
from django.utils import timezone


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['name', 'users', 'created_at']
    created_at = serializers.DateTimeField(default = timezone.now())

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['author', 'text', 'chat', 'created_at']
    created_at = serializers.DateTimeField(default = timezone.now())
=======
from .models import Message, Chat


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message 
        fields = ['chat', 'author', 'text', 'created_at']

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat 
        fields = ['name', 'users', 'created_at']
>>>>>>> origin/main
