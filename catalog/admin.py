from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class Category(admin.ModelAdmin):

    list_display = ('id', 'name', )
    search_fields = ('name', 'description', )

@admin.register(Product)
class Product(admin.ModelAdmin):

    list_display = ('id', 'name', 'price', 'category', )
    search_fields = ('name', 'description',)