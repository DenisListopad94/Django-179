from django.contrib import admin
from .models import *



class AdminAuto(admin.ModelAdmin):
    list_display = ('title', 'year_create','costs','speed')
    list_display_links = ('title',)
    search_fields = ('title', 'year_create','costs')
    list_editable = ('year_create','costs')
    list_filter = ('title', 'speed', 'year_create')
    # list_per_page = 3
    ordering = ('costs','-year_create')

admin.site.register(Auto,AdminAuto)
admin.site.register(Country)
admin.site.register(Provider)
admin.site.register(Director)
# Register your models here.
