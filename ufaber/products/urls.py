from django.contrib import admin
from django.urls import path,include
from .views import add_product,products,PostCreateAPIView,ListAllCategoryAPIView,ListSubcategoryAPIView,ListProductByCategoryAPIView,ListProductBySubcategoryAPIView

urlpatterns = [

    path('', products,name='products'),
    path('api/add-products/',PostCreateAPIView.as_view(), name="add__listproducts"),
    path('api/list-categories/',ListAllCategoryAPIView.as_view(), name="list_all_categories"),
    path('api/list-subcategories/',ListSubcategoryAPIView.as_view(), name="list_subcategory"),
    path('api/list-product-categories/',ListProductByCategoryAPIView.as_view(), name="list_product_category"),
    path('api/list-product-subcategories/',ListProductBySubcategoryAPIView.as_view(), name="list_product_subcategory"),
    path('api/add-product/',add_product, name="add_product"),
    
]
