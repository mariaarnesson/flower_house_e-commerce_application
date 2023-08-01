from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_category, name='blog_category'),
    path('post_list', views.post_list, name='post_list'),
    path('blog_post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('blog_post/<slug:slug>/like/', views.post_like, name='post_like'),
]