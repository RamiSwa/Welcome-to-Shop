from django.contrib import admin
from .models import Product
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'category', 'price', 'stock', 'available', 'created_date', 'modified_date']
    list_filter = ['available', 'created_date', 'modified_date', 'category']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('product_name',)}