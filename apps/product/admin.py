from django.contrib import admin

from .models import *

class ProductImagesInline(admin.TabularInline):
    model = ProductImage
    fields = ['image']


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesInline]
    list_display = ['id', 'title', 'price']
    list_display_links = ['id', 'title']

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
# admin.site.register(ProductImage, ProductImagesInline)

