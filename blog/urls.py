from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_category, name='blog_category'),
    path('post_list', views.post_list, name='post_list'),
]