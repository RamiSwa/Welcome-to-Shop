from django.contrib import admin
from .models import Product, Variation

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'category', 'price', 'stock', 'available', 'created_date', 'modified_date']
    list_filter = ['available', 'created_date', 'modified_date', 'category']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('product_name',)}  # Auto-generating slug from product name
    search_fields = ['product_name', 'category__category_name']  # Adding a search bar for easier navigation


@admin.register(Variation)
class VariationAdmin(admin.ModelAdmin):
    # Display product, variation type, value, and active status
    list_display = ['product', 'variation_category', 'variation_value', 'is_active']
    
    # Allow editing of whether the variation is active directly in the list view
    list_editable = ['is_active']
    
    # Add filters for better navigation, filtering by product and variation type (e.g., scent, material)
    list_filter = ['product', 'variation_category', 'variation_value']
    
    # Adding search fields for quick access to specific variations
    search_fields = ['product__product_name', 'variation_value']
