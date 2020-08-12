from django import forms
from products.models import Products

from django.utils.translation import ugettext_lazy as _


from django.forms import Form, ModelForm


class AddProductForm(forms.ModelForm):
    product_name = forms.CharField(label=_("Product Name *"),required=False)
    class Meta:
        model = Products
        fields = ['product_name', 'category', 'subcategory']
        labels  = {
        'category': 'Select Category ', 'category': 'Select Subcategory '
        }
