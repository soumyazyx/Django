from django.db import models


class City(models.Model):
    city = models.CharField(max_length=1000)

    def __str__(self):
        return self.city

    class Meta:
        verbose_name_plural = 'cities'
