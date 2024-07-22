from django.shortcuts import render

from products.models import Categories

def show_about_page(request):

    categories = Categories.objects.all()
    context = {
        'categories': categories
    }

    return render(request, "app/about.html", context)
