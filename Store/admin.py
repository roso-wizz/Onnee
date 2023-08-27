from django.contrib import admin
from .models import Category, Product

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',),}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'slug', 'price', 'inStock', 'created', 'updated']
    list_filter = ['inStock', 'isActive']
    list_editable = ['price', 'inStock']
    prepopulated_fields = {'slug': ('title',),}