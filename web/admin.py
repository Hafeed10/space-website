from django.contrib import admin
from .models import Contentitem, Item
from .models import Colum

class ContentitemAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'image']

class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'image']

class ColumsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'icon']

admin.site.register(Contentitem, ContentitemAdmin)


admin.site.register(Item, ItemAdmin)


admin.site.register(Colum, ColumsAdmin)  
