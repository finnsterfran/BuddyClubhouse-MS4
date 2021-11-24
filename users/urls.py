from django.urls import path
from . import views

urlpatterns = [
    path('', views.profiles, name='profiles'),
    path('login/', views.userLogin, name='login'),
    path('logout/', views.userLogout, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/<str:pk>/', views.profile, name='profile'),
    path('account/', views.account, name='account'),
    path('edit_account/', views.edit_account, name='edit_account'),
]