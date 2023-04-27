from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('addfile/', views.addfile, name='addfile'),
    path('change_theme/<str:theme>', views.change_theme, name='change_theme')
]