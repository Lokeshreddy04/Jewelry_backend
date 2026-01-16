from django.urls import path
from . import views
from .auth_views import register_user, login_user




urlpatterns = [
    # Product APIs
    path('users/register/', register_user),
    path('users/login/', login_user),
    path('products/', views.get_products),
    path('products/<int:id>/', views.get_product),
    path('products/add/', views.add_product),
    path('products/<int:id>/update/', views.update_product),
    path('products/<int:id>/delete/', views.delete_product),

    # Category APIs
    path('categories/', views.get_categories),
    path('categories/<int:id>/products/', views.get_products_by_category),
]
