from django.urls import path

from .views import index, products_list, product_details

urlpatterns = [
    path('', index, name='index'),
    path('products/<slug:category_slug>/', products_list, name='products-list'),
    path('products/details/<int:product_id>/', product_details, name='product-details'),
]