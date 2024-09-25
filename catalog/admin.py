from django.contrib import admin
from catalog.models import Category, Product, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('title', 'description',)


@admin.register(Version)
class VerdionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'product', 'is_active',)
