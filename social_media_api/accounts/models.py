from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following_users', blank=True)

    following = models.ManyToManyField('self', symmetrical=False, related_name='followers_users', blank=True)

    def __str__(self):
        return self.username