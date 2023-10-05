from rest_framework import serializers
from .models import Message, Chat


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message 
        fields = ['chat', 'author', 'text', 'created_at']

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat 
        fields = ['name', 'users', 'created_at']
