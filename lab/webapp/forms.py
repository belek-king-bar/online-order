from django import forms
from webapp.models import Food, OrderFood, Order

class OrderFoodForm(forms.ModelForm):
    class Meta:
        model = OrderFood
        exclude = []


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        exclude = []


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = []