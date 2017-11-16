from django.db import models
from django.utils import timezone


class Item(models.Model):
    date_created = models.DateTimeField(default=timezone.now)
    title = models.TextField()
    date_due = models.DateTimeField(default=timezone.now)
    completed_status = models.BooleanField(False)

    def __str__(self):
        return self.title

    def set_completed_status(self):
        self.date_created = timezone.now()
        self.save()
