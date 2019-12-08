from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=1000)
    addr = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
