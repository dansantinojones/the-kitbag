from django.db import models

# Create your models here.

class League(models.Model):
    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=50, null=False, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Shirt(models.Model):
    league = models.ForeignKey('League', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=250, null=True, blank=True)
    name = models.CharField(max_length=250)
    description = models.TextField()
    size = models.CharField(max_length=10, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class SellShirt(models.Model):
    team_name = models.CharField(max_length=250, null=False, blank=False)
    home_away_third = models.CharField(max_length=250, null=False, blank=False)
    league = models.CharField(max_length=250, null=False, blank=False)
    year = models.CharField(max_length=250, null=False, blank=False)
    size = models.CharField(max_length=10, null=False, blank=False)
    condition = models.CharField(max_length=250, null=False, blank=False)
    additional_info = models.TextField(null=True, blank=True)
    image_front = models.ImageField(null=False, blank=False)
    image_back = models.ImageField(null=False, blank=False)
    full_name = models.CharField(max_length=250, null=False, blank=False)
    email = models.CharField(max_length=250, null=False, blank=False)
    phone_number = models.CharField(max_length=250, null=False, blank=False)

    def __str__(self):
        return self.team_name
