from django.db import models
from django.urls import reverse
from category.models import Category

# Create your models here.


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