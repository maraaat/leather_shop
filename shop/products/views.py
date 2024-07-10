from django.shortcuts import render


# def show_catalog(request):
#     return render(request, "products/catalog.html")
#

def show_catalog(request):
    context = {
        "title": 'Каталог товаров | AMmade',
        'products':
            [
                {
                    'image': 'img/allproducts/products__thumb__01.jpg',
                    'name': 'Обложка для паспорта',
                    'description': 'Обложа для паспорта из кожи нитки трата',
                    'price': 2000
                },
                {
                    'image': 'img/allproducts/products__thumb__01.jpg',
                    'name': 'Докхолдер',
                    'description': 'Обложа для паспорта из кожи нитки трата',
                    'price': 3000
                },
                {
                    'image': 'img/allproducts/products__thumb__01.jpg',
                    'name': 'Кардхолдер',
                    'description': 'Обложа для паспорта из кожи нитки трата',
                    'price': 1000
                },
                {
                    'image': 'img/allproducts/products__thumb__01.jpg',
                    'name': 'Портмоне',
                    'description': 'Обложа для паспорта из кожи нитки трата',
                    'price': 4000
                },
                {
                    'image': 'img/allproducts/products__thumb__01.jpg',
                    'name': 'Брелок',
                    'description': 'Обложа для паспорта из кожи нитки трата',
                    'price': 500
                },
                {
                    'image': 'img/allproducts/products__thumb__01.jpg',
                    'name': 'Поясной ремень',
                    'description': 'Обложа для паспорта из кожи нитки трата',
                    'price': 7000
                },
            ]
    }
    return render(request, "products/catalog.html", context)
