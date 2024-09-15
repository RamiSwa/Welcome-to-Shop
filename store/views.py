from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404

from carts.models import CartItem
from carts.views import _cart_id
from .models import Product
from category.models import Category
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q


# Create your views here.


def store(request, category_slug=None):
    categories = None
    products = None
    
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.all().filter(category=categories, available=True)
        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)        
        product_count = products.count()
    else:
    
        products = Product.objects.all().filter(available=True).order_by('id')
        paginator = Paginator(products, 9)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    context = {
        'products': paged_products,
        'product_count': product_count,
        
    }
    return render(request, 'store/store.html', context=context)


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
        
        # Collect variation categories and their values
        variation_categories = {}
        for variation in single_product.variation_set.all():
            category = variation.variation_category
            if category not in variation_categories:
                variation_categories[category] = []
            variation_categories[category].append(variation)

    except Product.DoesNotExist:
        raise Http404("Product does not exist")

    context = {
        'single_product': single_product,
        'in_cart': in_cart,
        'variation_categories': variation_categories,
    }
    return render(request, 'store/product_detail.html', context=context)



def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            product_count = products.count()
    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)