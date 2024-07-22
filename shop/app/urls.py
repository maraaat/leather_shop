from django.contrib import admin
from django.urls import path, include

from .views import show_about_page

app_name = 'app'

urlpatterns = [
    path('', show_about_page, name='about')
]
