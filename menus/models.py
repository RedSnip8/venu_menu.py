from django.db import models
from stands.models import Stand

class Menus(models.Model):
    item_name = models.TextField(max_length=200)
    stand_code_name = models.ForeignKey(Stand, on_delete=models.DO_NOTHING)

