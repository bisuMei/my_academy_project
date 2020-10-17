from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Workout(models.Model):
    title = models.CharField(max_length=50)
    week = models.CharField(max_length=50)
    day = models.CharField(max_length=20)
    workout = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='user_workout')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'workout'
        verbose_name_plural = 'workouts'
