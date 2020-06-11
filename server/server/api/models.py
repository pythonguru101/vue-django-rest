from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models import (
    CASCADE,
    CharField,
    DateTimeField,
    ForeignKey,
    ManyToManyField,
    Model,
    TextField,
)


class User(AbstractUser):
    phone = CharField(max_length=20, blank=True, null=True)
    nick_name = CharField(max_length=20, blank=True, null=True)
    followers = ManyToManyField('self', related_name='follower', symmetrical=False)


class Shop(Model):
    user = ForeignKey(User, related_name='shops', on_delete=CASCADE)
    created = DateTimeField(auto_now_add=True)
    name = CharField(max_length=255)
    content = TextField(blank=True, null=True)
    updated = DateTimeField(auto_now=True)
