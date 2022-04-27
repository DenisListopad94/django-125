from django.contrib import admin
from cars.models import Car,Company
# Register your models here.


class CarsAdmin(admin.ModelAdmin):
    list_display = ('id','title','costs','create')
    list_display_links = ('id','title')
    search_fields = ('title','costs')
    list_editable = ('costs','create')
    list_filter = ('title','costs','create')
    # list_per_page = 2 # пагинация

admin.site.register(Car,CarsAdmin)
admin.site.register(Company)