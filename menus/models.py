from django.db import models
from stands.models import Stand
from products.models import Product

class Menu(models.Model):
    item_name = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    stand_code_name = models.ForeignKey(Stand, on_delete=models.DO_NOTHING)

