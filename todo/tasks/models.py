from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=500)
    content = models.CharField(max_length=2000)
    completed = models.BooleanField()

    def __str__(self):
        return self.title
