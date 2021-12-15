from django.urls import path
from . import views


urlpatterns = [
    path('', views.profiles, name='profiles'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),
    path('account/', views.user_account, name='account'),
    path('edit_account', views.edit_account, name='edit_account'),
    path('order_history/<order_number>/', views.order_history,
         name='order_history'),
]
