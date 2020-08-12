from django.contrib import admin
from products.models import Category,Subcategory,Products
# Register your models here.

admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Products)