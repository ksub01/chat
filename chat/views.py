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

