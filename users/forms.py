from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from captcha.fields import CaptchaField

from .models import *


class CustomUserCreationForm(UserCreationForm):
    captcha = CaptchaField(label='Капча(Заглавными)')

    class Meta:
        model = CustomUser
        fields = ('username', 'gender', 'email', 'birth_date')


class CustomUserChangeForm(UserChangeForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}), required=False)
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}), required=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'birth_date', 'avatar')


class ProfileChangeForm(UserChangeForm):
    avatar = forms.ImageField(label='Аватар', required=False)

    class Meta:
        model = Profile
        fields = ('avatar',)


class CustomUserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    captcha = CaptchaField(label='Капча(Заглавными)')
