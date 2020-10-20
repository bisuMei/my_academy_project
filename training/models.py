from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
# Create your models here.


class Workout(models.Model):
    title = models.CharField(max_length=50)
    week = models.CharField(max_length=50)
    day = models.CharField(max_length=20)
    workout = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='user_workout',
                               null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'workout'
        verbose_name_plural = 'workouts'


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    birth = models.DateTimeField(blank=True, null=True)
    photo = models.ImageField(upload_to="user/%Y/%m/%d", blank=True)

    def __str(self):
        return '{}profile'.format(self.user.first_name)
