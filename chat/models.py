from django.db import models


class User(models.Model):
    username = models.CharField(max_length=200, unique=True)

class Chat(models.Model):
    name = models.CharField(max_length=200, unique=True)
    users = models.ManyToManyField(User)
    created_at = models.DateTimeField()

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    created_at = models.DateTimeField()


