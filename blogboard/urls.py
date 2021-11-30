from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('write_blog/', views.write_blog, name='write_blog'),
    path('blog_entry/<str:pk>/', views.blog_entry, name='blog_entry'),
    path('edit_blog/<str:pk>/', views.edit_blog, name="edit_blog"),
    path('delete_blog/<str:pk>/', views.delete_blog, name='delete_blog'),
]
