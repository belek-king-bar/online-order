from django import forms
from webapp.models import Order, Food

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = []


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        exclude = []