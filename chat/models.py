from django.db import models
<<<<<<< HEAD


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


=======
import datetime
from django.contrib.auth.models import User
from django.utils import timezone


class Chat(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    users = models.ManyToManyField(User)
    def __str__(self):
        res = str(self.name) + " "
        for i in self.users.all():
            res += str(i) + " "
        return res

    

class Message(models.Model):
    def __str__(self):
        return str(self.chat) + " " + str(self.author) + " " + self.text + " "

    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now, blank=True)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.created_at <= now
>>>>>>> origin/main
