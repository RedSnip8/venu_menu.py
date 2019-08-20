from django.contrib import admin
from .models import Menu

class MenuAdmin(admin.ModelAdmin):
  list_display = ('id', 'item_name', 'stand_code_name')
  search_fields = ('item_name__name', 'stand_code_name__code_name')
  list_per_page = 30


admin.site.register(Menu, MenuAdmin)