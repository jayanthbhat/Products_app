from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,CreateAPIView,RetrieveUpdateAPIView
from .serializers import ProductSerializer,ListAllCategorySerializer,ListSubcategorySerializer
from products.models import Products,Category,Subcategory
from products.forms import AddProductForm
import json
from django.core.serializers.json import DjangoJSONEncoder

class PostCreateAPIView(ListCreateAPIView):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        return Products.objects.all()  
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            product_name = serializer.data['product_name']
            category_id = serializer.data['category']
            subcategory_id = serializer.data['subcategory']
            try:
                category=Category.objects.get(id=category_id)
                subcategory=Subcategory.objects.get(id=subcategory_id,category=category)
                pd=Products.objects.create(product_name=product_name,subcategory=subcategory,category=category)
                content = {"success":"Product Added Successfully"}
                return Response(content,status=status.HTTP_200_OK)
            except Category.DoesNotExist:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ListAllCategoryAPIView(ListAPIView):
    serializer_class = ListAllCategorySerializer
    def get_queryset(self):
        # current_user = self.request.user
        return Category.objects.all()  

class ListSubcategoryAPIView(ListAPIView):
    serializer_class = ListSubcategorySerializer 
    def get_queryset(self):
           
        category_id = self.request.query_params.get('category_id', None)
        if category_id:
            return Subcategory.objects.filter(category__id=category_id)
        else:
            return Subcategory.objects.all()

class ListProductByCategoryAPIView(ListAPIView):
    serializer_class = ProductSerializer 
    def get_queryset(self):
           
        category_id = self.request.query_params.get('category_id', None)
        if category_id:
            return Products.objects.filter(category__id=category_id)
        else:
            return Products.objects.all()


class ListProductBySubcategoryAPIView(ListAPIView):
    serializer_class = ProductSerializer 
    def get_queryset(self):
           
        subcategory_id = self.request.query_params.get('subcategory_id', None)
        if subcategory_id:
            return Products.objects.filter(subcategory__id=subcategory_id)
        else:
            return Products.objects.all()

def products(request):
    products=Products.objects.all()
    categories=Category.objects.all()
    sub_categories=Subcategory.objects.all()
    
    sub=[]
    for i in sub_categories:

        sub.append({
            "subcategory_name":i.subcategory_name,
            "subcategory_id":i.id,
            "category":i.category.id,
        })
    subcategory_json = json.dumps(list(sub), cls=DjangoJSONEncoder)
    form=AddProductForm()  
    context = {"products":products,"form":form,"categories":categories,'sub_categories':sub_categories,'subcategory_json':subcategory_json}
    return render(request,'application_app/home.html',context)

def add_product(request):
    if request.method == 'POST':
            product_name = request.POST.get('product_name')
            category_id = request.POST.get('category')
            subcategory_id = request.POST.get('subcategory')
            try:
                category=Category.objects.get(id=category_id)
                subcategory=Subcategory.objects.get(id=subcategory_id,category=category)
                pd=Products.objects.create(product_name=product_name,subcategory=subcategory,category=category)
                success="Product Added Successfully"
                context = {"products":products,"form":form,"categories":categories,'sub_categories':sub_categories,"success":success}
                return render(request,'application_app/home.html',context)
            except Category.DoesNotExist:
                return Response(status=status.HTTP_400_BAD_REQUEST)
    form=AddProductForm()  
    context = {"products":products,"form":form,"categories":categories,'sub_categories':sub_categories,}
    return render(request,'application_app/home.html',context)