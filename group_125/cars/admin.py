from django.contrib import admin
from cars.models import *
# Register your models here.


class CarsAdmin(admin.ModelAdmin):
    list_display = ('id','title','costs','create')
    list_display_links = ('id','title')
    search_fields = ('title','costs')
    list_editable = ('costs','create')
    list_filter = ('title','costs','create')
    filter_horizontal = ('provider',)
    ordering = ('title','id')
    # list_per_page = 2 # пагинация

class DirectorAdmin(admin.ModelAdmin):
    list_display = ('id','name','company')
    list_display_links = ('id','name')

admin.site.register(Car,CarsAdmin)
admin.site.register(Company)
admin.site.register(Provider)
admin.site.register(Director,DirectorAdmin)