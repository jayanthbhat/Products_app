from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return str(self.category_name)


class Subcategory(models.Model):
    category = models.ForeignKey("Category", related_name='subcategory_category', on_delete=models.CASCADE, blank=True, null=True)
    subcategory_name = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return str(self.subcategory_name)


class Products(models.Model):
    product_name = models.CharField(max_length=200,null=True,blank=True)
    category = models.ForeignKey("Category", related_name='product_category', on_delete=models.CASCADE, blank=True, null=True)
    subcategory = models.ForeignKey("Subcategory", related_name='product_subcategory', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.product_name)