from django.db import models


class Message(models.Model):
    time = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
