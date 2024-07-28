from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from shop import settings

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('catalog/', include("products.urls", namespace='cat')),
    path('', include("app.urls", namespace='main')),
    path('user/', include("users.urls", namespace='user'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)