from django.contrib import admin
from stands.models import Stand

class StandAdmin(admin.ModelAdmin):
  list_display = ('id', 'code_name', 'is_open' )
  list_display_links = ('id', 'code_name')
  list_editable = ('is_open',)
  search_fields = ('code_name', 'id')
  list_per_page = 10

admin.site.register(Stand, StandAdmin)