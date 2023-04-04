from django.urls import path
from .views import searchProduct, searchCategory, addProduct, updateProduct 

urlpatterns = [
    path('', searchProduct.as_view(), name='search_product'),
    path('add/', addProduct.as_view(), name='add_product'),
    path('update/', updateProduct.as_view(), name='update_product'),
    path('category/', searchCategory.as_view(), name='search_category'),
    
]



