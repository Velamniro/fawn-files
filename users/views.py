from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from home.utils import get_theme
from .forms import CustomUserCreationForm, CustomUserLoginForm
from .models import Profile, CustomUser


class RegisterUser(CreateView):
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

    def get_context_data(self, *args, **kwargs):
        context = super(RegisterUser, self).get_context_data(*args, **kwargs)
        context['theme'] = get_theme(self.request)
        return context


class LoginUser(LoginView):
    form_class = CustomUserLoginForm
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        context = super(LoginUser, self).get_context_data(*args, **kwargs)
        context['theme'] = get_theme(self.request)
        return context


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'users/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        profile = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['profile'] = profile
        user = profile.user
        if user.gender == 'm':
            context['gender'] = 'Мужчина'
        elif user.gender == 'f':
            context['gender'] = 'Женщина'
        context['theme'] = get_theme(self.request)
        return context


class EditProfile(LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name_suffix = '_update_form'
    fields = ['username', 'gender', 'avatar', 'birth_date']
    login_url = 'login'

    def get_context_data(self, *args, **kwargs):
        context = super(EditProfile, self).get_context_data(*args, **kwargs)
        user = get_object_or_404(CustomUser, id=self.kwargs['pk'])
        context['profile'] = user.profile
        context['theme'] = get_theme(self.request)
        return context

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')
