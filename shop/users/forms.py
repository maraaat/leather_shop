from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import User


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('email', 'password')


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'username', 'fio', 'phone', 'password1', 'password2')

    email = forms.EmailField()
    username = forms.CharField()
    fio = forms.CharField()
    phone = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()


class UserSetChangesForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'fio', 'phone']

    email = forms.EmailField()
    username = forms.CharField()
    fio = forms.CharField()
    phone = forms.CharField()