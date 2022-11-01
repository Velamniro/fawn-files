from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('<int:pk>/', views.ShowProfilePageView.as_view(), name='user_profile'),
    path('edit_profile/<int:pk>/', views.EditProfile.as_view(), name='edit_profile'),
]
