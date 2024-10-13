from django import forms
from .models import Products, Sales

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'

        # labels
        labels = {
            'product_name': 'Product Name',
            'product_info': 'Product Info',
            'product_price': 'Product Price',
            'product_stock': 'Product Stock'
        }

        # widgets
        widgets = {
            'product_name': forms.TextInput(attrs={'placeholder': 'Add product name...', 'class': 'form-control'}),
            'product_info': forms.Textarea(attrs={'placeholder': 'Add product info...', 'class': 'form-control'}),
            'product_price': forms.NumberInput(attrs={'placeholder': 'Add product price...', 'class': 'form-control'}),
            'product_stock': forms.NumberInput(attrs={'placeholder': 'Add product stock...', 'class': 'form-control'}),
        }

