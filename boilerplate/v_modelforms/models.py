from django.db import models


class Blog(models.Model):
    title = models.TextField()
    content = models.TextField()

    def __str__(self):
        return self.title
