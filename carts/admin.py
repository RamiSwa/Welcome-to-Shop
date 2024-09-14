from django.contrib import admin
from .models import Cart, CartItem

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1
    readonly_fields = ('sub_total',)
    fields = ('product', 'quantity', 'sub_total', 'is_active')

class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'date_added')
    search_fields = ('cart_id',)
    readonly_fields = ('date_added',)
    inlines = [CartItemInline]  # Display associated cart items in the Cart admin

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'cart', 'user', 'quantity', 'is_active', 'sub_total')
    list_filter = ('is_active', 'product', 'user')
    search_fields = ('product__product_name', 'cart__cart_id', 'user__email')
    readonly_fields = ('sub_total',)

# Register models in the admin site
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
