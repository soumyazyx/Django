from django.db import models


class City(models.Model):
    city = models.TextField()

    def __str__(self):
        return self.city

    class Meta:
        verbose_name_plural = 'cities'
