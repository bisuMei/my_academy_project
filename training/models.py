from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
# Create your models here.


class Workout(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    workout_body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_workout', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'workout'
        verbose_name_plural = 'workouts'

    def get_absolute_url(self):
        return reverse('training:workout_details', args=[str(self.id)])


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    birth = models.DateTimeField(blank=True, null=True)
    photo = models.ImageField(upload_to="user/%Y/%m/%d", blank=True)

    def __str__(self):
        return '{} profile'.format(self.user.username)


class Comment(models.Model):
    workout = models.ForeignKey(Workout,
                                on_delete=models.CASCADE,
                                related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)