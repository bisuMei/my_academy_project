from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Workout)
admin.site.register(models.Profile)
admin.site.register(models.Comment)