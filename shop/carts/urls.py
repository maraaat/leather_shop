from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'carts'

urlpatterns = [
    path('cart', views.show_cart, name='cart'),
]
