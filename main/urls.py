from django.urls import path
from .views import searchProduct

urlpatterns = [
    path('', searchProduct.as_view(), name='search_product'),
]



