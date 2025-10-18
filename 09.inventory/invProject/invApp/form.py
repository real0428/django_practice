from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
  class Meta:
    model = Product
    fields = '__all__'
    labels = {
      'product_id': 'ID',
      'name': '品名',
      'sku': '單位',
      'price': '單價',
      'quantity': '數量',
      'supplier': '供應商',
    }

    error_messages = {
      'name': {
        'required': '必填',
        'max_length': '最多不可超過100字'
      },
      'sku': {
        'required': '必填',
        'max_length': '最多不可超過50字'
      },
      'price': {
        'required': '必填',
      },
      'quantity': {
        'required': '必填',
      },
      'supplier': {
        'required': '必填',
      },
    }

    widgets = {
      'product_id': forms.NumberInput(attrs={'class': 'form-control'}),
      'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'請輸入商品名稱'}),
      'sku': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'請輸入單位'}),
      'price': forms.NumberInput(attrs={'class': 'form-control'}),
      'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
      'supplier': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'請輸入供應商'}),
    }
