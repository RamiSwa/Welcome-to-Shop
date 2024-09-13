from django.db import models
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=160, unique=True)
    description = models.TextField(blank=True, null=True)
    cat_image = models.ImageField(upload_to='photo/category', blank=True, null=True)

    class Meta:
        ordering = ['category_name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse('products_by_category', args=[self.slug])