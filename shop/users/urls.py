from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login, name="login"),
    path('reg/', views.reg, name="reg"),
    path('profile/', views.profile, name="profile"),
    path('history/', views.history, name="history"),
    path('logout/', views.logout, name="logout"),

]

