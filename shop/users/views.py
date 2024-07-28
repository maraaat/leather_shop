from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from django.urls import reverse

from django.contrib.auth import authenticate, login

from products.models import Categories

from .forms import UserLoginForm
from .models import User

def login(request):
    categories = Categories.objects.all()
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = UserLoginForm()
    context = {
        'categories': categories,
        'form': form,
    }
    return render(request, "users/login.html", context)


def reg(request):
    categories = Categories.objects.all()
    form = UserLoginForm
    context = {
        'categories': categories,
        'form': form,
    }
    return render(request, "users/registration.html", context)


def logout(request):
    categories = Categories.objects.all()
    context = {
        'categories': categories,
    }
    auth.logout(request)
    return HttpResponseRedirect(reverse('user:login'))

def profile(request):
    categories = Categories.objects.all()
    context = {
        'categories': categories,
        'user': request.user
    }
    if request.user.is_authenticated:
        return render(request, "users/profile.html", context)
    else:
        return render(request, "users/login.html", context)


def history(request):
    categories = Categories.objects.all()
    context = {
        'categories': categories,
    }
    if request.user.is_authenticated:
        return render(request, "users/order_history.html", context)
    else:
        return render(request, "users/login.html", context)


def save_changes(request):



