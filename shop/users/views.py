from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from products.models import Categories

from .forms import UserLoginForm, UserSetChangesForm, UserRegistrationForm
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
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)

        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = UserRegistrationForm()

    context = {
        'categories': categories,
        'form': form,
    }
    return render(request, "users/registration.html", context)


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('user:login'))


@login_required
def profile(request):
    categories = Categories.objects.all()

    if request.method == 'POST':
        form = UserSetChangesForm(data=request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = UserSetChangesForm(instance=request.user)

    context = {
        'categories': categories,
        'form': form
    }

    return render(request, "users/profile.html", context)


@login_required
def history(request):
    categories = Categories.objects.all()
    context = {
        'categories': categories,
    }

    return render(request, "users/order_history.html", context)

