from django.contrib import admin
from .models import Product, Variation
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'category', 'price', 'stock', 'available', 'created_date', 'modified_date']
    list_filter = ['available', 'created_date', 'modified_date', 'category']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('product_name',)}
    

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('product', 'variation_category', 'variation_value')
    
    
admin.site.register(Variation, VariationAdmin)