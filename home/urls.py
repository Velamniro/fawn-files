from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('faq/', views.faq, name='faq'),
    path('change_theme/<str:theme>', views.change_theme, name='change_theme')
]