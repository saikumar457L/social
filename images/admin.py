from django.contrib import admin

from .models import Image

# Register your models here.

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ["title","image","created"]
    search_fields = ['title',"slug","description"]
    date_hierarchy = 'created'
    list_filter = ["created"]
