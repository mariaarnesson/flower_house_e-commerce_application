from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<product_id>', views.product_detail, name='product_detail'),
    path('products/add_to_favorites/<int:product_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('remove_from_favorites/<int:product_id>/', views.remove_from_favorites, name='remove_from_favorites'),
    path('products/favorites/', views.favorites, name='favorites'),
]