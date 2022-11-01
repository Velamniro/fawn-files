from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from django.core.exceptions import PermissionDenied

from home.utils import *
from .forms import CustomUserCreationForm, CustomUserLoginForm
from .models import Profile, CustomUser


class RegisterUser(DataMixin, CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')

    # Custom post
    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            Profile.objects.create(user=user)
            login(self.request, user)
            return redirect('home')
        else:
            return render(request, self.template_name, {'form': form})

    def get_context_data(self, **kwargs):
        context = super(RegisterUser, self).get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))


class LoginUser(DataMixin, LoginView):
    form_class = CustomUserLoginForm
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super(LoginUser, self).get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))


class ShowProfilePageView(DataMixin, DetailView):
    model = Profile
    template_name = 'users/user_profile.html'

    def get_context_data(self, **kwargs):
        context = super(ShowProfilePageView, self).get_context_data(**kwargs)
        profile = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['profile'] = profile
        user = profile.user
        if user.gender == 'm':
            context['gender'] = 'Мужчина'
        elif user.gender == 'f':
            context['gender'] = 'Женщина'
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))


class EditProfile(LoginRequiredMixin, DataMixin, UpdateView):
    model = CustomUser
    template_name_suffix = '_update_form'
    fields = ['username', 'gender', 'avatar', 'birth_date']
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super(EditProfile, self).get_context_data(**kwargs)
        user = get_object_or_404(CustomUser, id=self.kwargs['pk'])
        context['profile'] = user.profile
        if self.request.user.id != user.id:
            raise PermissionDenied()
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')
