from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView
from webapp.models import User, Order, Food
from webapp.forms import OrderForm, FoodForm
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404

# Create your views here.

class OrderListView(ListView, FormView):
    model = Order
    template_name = 'order_list.html'


class UserListView(ListView):
    model = User
    template_name = 'user_list.html'


class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_detail.html'


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'order_create.html'
    success_url = reverse_lazy('article_list')


class FoodDetailView(DetailView):
    model = Food
    template_name = 'food_detail.html'


class FoodCreateView(CreateView):
    model = Food
    form_class = FoodForm
    template_name = 'food_create.html'


    def get_success_url(self):
        return reverse('food_detail', kwargs={'pk': self.object.pk})


class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'order_update.html'

    def get_success_url(self):
        return reverse('order_detail', kwargs={'pk': self.object.pk})


class FoodUpdateView(UpdateView):
    model = Food
    form_class = FoodForm
    template_name = 'food_update.html'

    def get_success_url(self):
        return reverse('food_detail', kwargs={'pk': self.object.pk})