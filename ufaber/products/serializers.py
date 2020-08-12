from rest_framework import serializers

from products.models import * 


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields=[
            'id',
            'product_name',
            'category',
            'subcategory'
        ]
    def validate(self, data):
        if data['product_name'] == '':
            raise serializers.ValidationError('Enter Product name')
        if data['category'] == 'None' or data['category'] == None:
            raise serializers.ValidationError('Select Category')
        if data['subcategory'] == 'None' or data['subcategory'] == None:
            raise serializers.ValidationError('Select SubCategory')
        
        return data


class ListAllCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id',
            'category_name']

class ListSubcategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Subcategory
        fields = ['id',
            'category',
            'subcategory_name']

