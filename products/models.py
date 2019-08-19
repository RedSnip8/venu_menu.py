from django.db import models

class Product(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField(blank=True)
    is_avaiable = models.BooleanField(default=True)
    is_promoted = models.BooleanField(default=False)

    def __str__(self):
      return self.name