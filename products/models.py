from django.db import models

class Product(models.Model):

    CATEGORY_CHOICES = [
      ('food','Food'),
      ('nonalc','Non-Alcoholic'),
      ('liq','Liquor'),
      ('dombeer','Domestic Beer'),
      ('craftbeer','Craft Beer'),
      ('prembeer','Premium Beer')
    ]

    name = models.CharField(max_length = 200)
    category = models.CharField(max_length=200, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%y/%m/%d', blank=True)
    is_available = models.BooleanField(default=True)
    is_promoted = models.BooleanField(default=False)

    def __str__(self):
      return self.name