from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import viewsets, generics, permissions, status
from django.shortcuts import get_object_or_404
from django.db.models import ProtectedError
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

# Create your views here.
from .models import *
from .serializers import *
from django.contrib.auth.models import User

class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    def get_queryset(self):
        queryset = Customer.objects.filter(shop=self.request.user.employee.shop)
        return queryset

class CurrencyViewSet(viewsets.ModelViewSet):
    
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = CustomerSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    def get_queryset(self):
        queryset = Category.objects.filter(shop=self.request.user.employee.shop)
        return queryset

class BrandViewSet(viewsets.ModelViewSet):
    serializer_class = BrandSerializer
    def get_queryset(self):
        queryset = Brand.objects.filter(shop=self.request.user.employee.shop)
        return queryset
   
class ShopViewSet(viewsets.ModelViewSet):
    
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer



class InvoiceViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    serializer_class = InvoiceSerializer
    def get_queryset(self):
        customer_items = Customer.objects.filter(shop=self.request.user.employee.shop)
        queryset = Invoice.objects.filter(customer__in=customer_items.values_list('pk'))
        return queryset


class InvoiceItemViewSet(viewsets.ModelViewSet):
    
    serializer_class = InvoiceItemSerializer
    queryset = InvoiceItem.objects.all()