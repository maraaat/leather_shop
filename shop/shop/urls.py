from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog', include("products.urls"), name="catalog"),
    path('about', include("app.urls"), name="about")
]
