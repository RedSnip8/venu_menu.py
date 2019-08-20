from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'category', 'is_available', 'is_promoted')
  list_display_links = ('id', 'name')
  list_editable = ('is_available', 'is_promoted')
  search_fields = ('id', 'name', 'category')
  list_per_page = 20

admin.site.register(Product, ProductAdmin)