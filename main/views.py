from django.shortcuts import render
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from rest_framework import generics
from rest_framework import permissions




#create a search view for products
class searchProduct(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        query = self.request.query_params.get('q')
        return Product.objects.filter(name__icontains=query)