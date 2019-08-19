from django.db import models

class Stand(models.Model):
    name = models.CharField(max_length = 200)
    code_name = models.CharField(max_length = 200)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    is_open = models.BooleanField(default=True)

    def __str__(self):
      return self.code_name