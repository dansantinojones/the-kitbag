from django.db import models


class Newsletter(models.Model):
    email = models.CharField(max_length=100, unique=True, null=False, blank=False)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
