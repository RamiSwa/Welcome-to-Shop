from django.contrib import admin
from .models import Payment, Order, OrderProduct

# Payment Admin
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('payment_id', 'user', 'payment_method', 'amount_paid', 'status', 'created_at')
    list_filter = ('status', 'payment_method')
    search_fields = ('payment_id', 'user__email', 'status')
    list_per_page = 20

# OrderProduct Inline
class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('user', 'product', 'variations', 'quantity', 'product_price')
    extra = 0

# Order Admin
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'full_name', 'phone', 'email', 'city', 'order_total', 'tax', 'status', 'is_ordered', 'created_at')
    list_filter = ('status', 'is_ordered', 'created_at')
    search_fields = ('order_number', 'first_name', 'last_name', 'email', 'phone')
    list_per_page = 20
    inlines = [OrderProductInline]

# OrderProduct Admin
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'user', 'quantity', 'product_price', 'ordered', 'created_at')
    list_filter = ('ordered', 'created_at', 'updated_at')
    search_fields = ('order__order_number', 'product__product_name', 'user__email')
    list_per_page = 20

# Register the models in the admin interface
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct, OrderProductAdmin)
