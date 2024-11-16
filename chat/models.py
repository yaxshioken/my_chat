from django.contrib.auth.models import User
from django.db import models
from django.db.models import SET_NULL

from config import settings


class Room(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    body = models.TextField()
    room = models.ForeignKey(Room, models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    reply = models.ForeignKey("self", on_delete=SET_NULL, null=True)
