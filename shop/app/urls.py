from django.contrib import admin
from django.urls import path, include

from .views import show_about_page, show_order_page, show_care_page

app_name = 'app'

urlpatterns = [
    path('about', show_about_page, name='about'),
    path('order', show_order_page, name='order'),
    path('care', show_care_page, name='care'),
]
