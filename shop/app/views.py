from django.shortcuts import render

from products.models import Categories


def show_about_page(request):
    categories = Categories.objects.all()
    context = {
        'categories': categories
    }

    return render(request, "app/about.html", context)


def show_order_page(request):
    categories = Categories.objects.all()
    context = {
        'categories': categories
    }

    return render(request, "app/order.html", context)


def show_care_page(request):
    categories = Categories.objects.all()
    context = {
        'categories': categories
    }

    return render(request, "app/care.html", context)
