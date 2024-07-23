from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'products'

urlpatterns = [
    path('', views.show_catalog, name="catalog"),
    path('category/<slug:category_slug>/', views.show_category_items, name="category"),
    path('product/<slug:product_slug>/', views.show_item, name='product'),
    path('search/', views.catalog_search, name="search"),
]

