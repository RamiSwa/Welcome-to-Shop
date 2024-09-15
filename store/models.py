from django.db import models
from django.urls import reverse
from category.models import Category

class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=600, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/products/', blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['product_name']
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.product_name

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])


class VariationManager(models.Manager):
    def personalization(self):
        return super(VariationManager, self).filter(variation_category='personalization', is_active=True)

    def scent(self):
        return super(VariationManager, self).filter(variation_category='scent', is_active=True)

    def packaging(self):
        return super(VariationManager, self).filter(variation_category='packaging', is_active=True)

    def material(self):
        return super(VariationManager, self).filter(variation_category='material', is_active=True)

    def arrangement(self):
        return super(VariationManager, self).filter(variation_category='arrangement', is_active=True)


variation_category_choice = (
    ('personalization', 'Personalization'),  # For engraving, name customization
    ('scent', 'Scent'),                      # For candles or scented products
    ('packaging', 'Packaging'),              # Gift wrapping options
    ('material', 'Material'),                # For handmade products like jewelry/sculptures
    ('arrangement', 'Flower Arrangement'),   # For flower arrangements
)

class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_category = models.CharField(max_length=100, choices=variation_category_choice)
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now=True)

    objects = VariationManager()

    def __str__(self):
        return f"{self.variation_category}: {self.variation_value}"
