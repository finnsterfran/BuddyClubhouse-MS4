from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('write_blog/', views.write_blog, name='write_blog'),
]