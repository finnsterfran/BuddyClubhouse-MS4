from django.urls import path
from . import views

urlpatterns = [
    path('', views.profiles, name='profiles'),
    path('login/', views.userLogin, name='login'),
    path('logout/', views.userLogout, name='logout'),
    path('register/', views.userRegister, name='register'),
    path('profile/<str:pk>/', views.profile, name='profile'),
    path('account/', views.userAccount, name='account'),
    path('edit_account', views.edit_account, name='edit_account'),
    path('order_history/<order_number>/', views.order_history, name='order_history'),
]
