from django.shortcuts import render
from .models import Categories, Products


def show_catalog(request):
    categories = Categories.objects.all()
    products = Products.objects.all()
    context = {
        'categories': categories,
        "title": 'Каталог товаров | AMmade',
        'products': products
    }
    return render(request, "products/catalog.html", context)


def show_item(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    context = {
        'product': product
    }
    return render(request, "products/product.html", context)

def show_category_items(request, category_slug):
    categories = Categories.objects.all()

    category = Categories.objects.get(slug=category_slug)
    if category_slug=="vse-tovary":
        return show_catalog(request)
    products = Products.objects.filter(category=category)
    context = {
        'categories': categories,
        "title": 'Каталог товаров | AMmade',
        'products': products
    }
    return render(request, "products/catalog.html", context)