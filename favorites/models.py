from django.db import models

class Favorite(models.Model):

    user = models.IntegerField()
    item = models.IntegerField()
