from django.urls import path

from .views import HomePageView, ProductDetail, ProductsListView

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('products/<slug:category_slug>/', ProductsListView.as_view(), name='products-list'),
    path('products/details/<int:pk>/', ProductDetail.as_view(), name='product-details'),
]