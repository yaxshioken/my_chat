from django.contrib.auth.models import AbstractUser
from django.db.models import ImageField, Model, ForeignKey, CASCADE, ManyToManyField, TextField


class Account(AbstractUser):
    avatar = ImageField(upload_to="avatars")
    bio = TextField()
    following = ManyToManyField("self", related_name="followers", symmetrical=False, blank=True)

