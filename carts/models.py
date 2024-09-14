from django.core.exceptions import ValidationError
from django.db import models
from store.models import Product, Variation
from accounts.models import Account

class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True, unique=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variations = models.ManyToManyField(Variation, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f'{self.product.product_name} - {self.quantity}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'product', 'cart'], name='unique_cartitem_for_user_or_cart')
        ]

    def clean(self):
        if not self.user and not self.cart:
            raise ValidationError("Either user or cart must be set for a CartItem.")
        if self.quantity <= 0:
            raise ValidationError("Quantity must be greater than zero.")

    def save(self, *args, **kwargs):
        self.clean()  # Ensure validation is performed before saving
        super().save(*args, **kwargs)
