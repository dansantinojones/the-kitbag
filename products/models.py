from django.db import models

# Create your models here.

class Leagues(models.Model):
    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=50, null=False, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Shirt(models.Model):
    leagues = models.ForeignKey('Leagues', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=250, null=True, blank=True)
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
