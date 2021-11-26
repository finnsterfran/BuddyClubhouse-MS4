from django.urls import path
from . import views

urlpatterns = [
    path('', views.dogs, name='dogs'),
    path('dog_profile/<str:pk>/', views.dog_profile, name='dog_profile'),
]
