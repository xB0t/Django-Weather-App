from django.db import models

class City(models.Model):
    city = models.CharField(max_length=10,verbose_name = "City Name")
    def __str__(self):
        return self.city
    class Meta:
        ordering = ["city"]
        verbose_name_plural = "Cities"