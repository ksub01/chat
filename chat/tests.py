<<<<<<< HEAD
from django.test import TestCase

# Create your tests here.
=======
import datetime

from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Message, Chat
from .serializers import *


class ChatModelTests(APITestCase):

    def setUp(self):
        user = User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")

    def test_creating_chat(self):
        chat = Chat.objects.create(name='gaming')
        self.assertEqual(chat.name, Chat.objects.get(pk=1).name)


class MessageModelTests(APITestCase):
    def setUp(self):
        user = User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")

    def test_creating_message(self):
        chat = Chat.objects.create(name='game')
        chat.users.set([User.objects.get(pk=1)])
        message = Message.objects.create(chat=chat, text='yes', author=User.objects.get(pk=1))
        self.assertEqual(Message.objects.get(pk=1).text, message.text)  

    def test_was_published_recently_with_future_message(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_message = Message(created_at=time)
        self.assertIs(future_message.was_published_recently(), False)


class ChatViewTests(APITestCase):
    def setUp(self):
        user = User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")

    def test_no_messages(self):
        url = reverse('messages-list') 
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

    def test_no_chats(self):
        url = reverse('chats-list') 
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

    def test_creating_one_chat(self):
        url = reverse('chats-list') 
        now = datetime.datetime.now().isoformat() + 'Z'
        user_id = 1
        new_chat = {'name': 'gaming', 'users':[user_id], 'created_at': now}
        res = self.client.post(url, new_chat)

        url = reverse('chats-detail', args=[1])
        response = self.client.get(url) 

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Chat.objects.count(), 1)
        self.assertEqual(Chat.objects.get().name, 'gaming')

    def test_creating_two_chats(self):
        url = reverse('chats-list') 
        now = datetime.datetime.now().isoformat() + 'Z'
        user_id = 1
        new_chat_1 = {'name': 'pool1', 'users':[user_id], 'created_at': now}
        res = self.client.post(url, new_chat_1)
        new_chat_2 = {'name': 'pool2', 'users':[user_id], 'created_at': now}
        res = self.client.post(url, new_chat_2)

        url = reverse('chats-list')
        response = self.client.get(url) 

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Chat.objects.count(), 2)
        self.assertEqual(Chat.objects.get(pk=1).name, 'pool1')
        self.assertEqual(Chat.objects.get(pk=2).name, 'pool2')

    def test_creating_one_message(self):
        
        user_id = 1
        chat_url = reverse('chats-list')
        res = self.client.post(chat_url, {'users': user_id, 'name': 'video'})

        now = datetime.datetime.now().isoformat() + 'Z'
        new_message = {'author': user_id, 'chat': 1, 'text': 'nonono', 'created_at': now}

        messages_url = reverse('messages-list') 
        response = self.client.post(messages_url, new_message)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED) 

        message_url = reverse('messages-detail', args=[1]) 
        result = self.client.get(message_url)
        self.assertEqual(Message.objects.count(), 1)
        self.assertEqual(Message.objects.get().text, 'nonono')


    def test_creating_two_message_in_one_chat(self):
        
        user_id = 1
        chat_url = reverse('chats-list')
        res = self.client.post(chat_url, {'users': user_id, 'name': 'video'})

        now = datetime.datetime.now().isoformat() + 'Z'
        new_message_1 = {'author': user_id, 'chat': 1, 'text': 'nonono1', 'created_at': now}

        messages_url = reverse('messages-list') 
        response_1 = self.client.post(messages_url, new_message_1)
        self.assertEqual(response_1.status_code, status.HTTP_201_CREATED) 

        message_url = reverse('messages-detail', args=[1]) 
        created_response = self.client.get(message_url)

        new_message_2 = {'author': user_id, 'chat': 1, 'text': 'nonono2', 'created_at': now}
        response_2 = self.client.post(messages_url, new_message_2)
        self.assertEqual(response_2.status_code, status.HTTP_201_CREATED) 

        message_url = reverse('messages-detail', args=[2]) 
        created_response = self.client.get(message_url)

        self.assertEqual(created_response.status_code, status.HTTP_200_OK) 
        self.assertEqual(Message.objects.count(), 2)
        self.assertEqual(Message.objects.get(pk=1).text, 'nonono1')
        self.assertEqual(Message.objects.get(pk=2).text, 'nonono2')

>>>>>>> origin/main
