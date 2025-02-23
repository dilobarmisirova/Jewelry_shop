from django import forms
from .models import OrderModel


class OrderModelForm(forms.ModelForm):
    class Meta:
        model = OrderModel
        exclude = ['user', 'product', 'created_at', 'total_price']

