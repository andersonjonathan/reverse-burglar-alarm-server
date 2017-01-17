import datetime
from django.db import models


class Message(models.Model):
    time = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    message = models.CharField(max_length=255)

    class Meta:
        ordering = ("-time",)

    def __str__(self):
        return str(self.dt) + " " + self.type + " " + self.message

    @property
    def dt(self):
        try:
            return datetime.datetime.strptime(self.time, "%Y-%m-%dT%H:%M:%S.%f") + datetime.timedelta(hours=1)
        except:
            return self.time
