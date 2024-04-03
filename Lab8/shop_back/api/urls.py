from django.urls import path
from api.views import categories, category_detail, products, product_detail, category_products

urlpatterns = [
    path('products/', products),
    path('products/<int:id>/', product_detail),
    path('categories/', categories),
    path('categories/<int:id>/', category_detail),
    path('categories/<int:id>/products/', category_products)
]