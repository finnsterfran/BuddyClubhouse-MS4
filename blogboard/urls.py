from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('write_blog/', views.write_blog, name='write_blog'),
    path('blog_post/<str:pk>/', views.blog_post, name='blog_post'),
    path('edit_blog/<str:pk>/', views.edit_blog, name="edit_blog"),
    path('delete_blog/<str:pk>/', views.delete_blog, name="delete_blog"),
]
