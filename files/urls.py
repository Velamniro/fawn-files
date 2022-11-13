from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>/', views.FilesDetailView.as_view(), name='file-detail')
]