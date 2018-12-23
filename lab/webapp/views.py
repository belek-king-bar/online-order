from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView, View
from django.http import HttpResponseRedirect
from webapp.models import User, Order, Food, OrderFood
from webapp.forms import OrderFoodForm, FoodForm, OrderForm
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404

# Create your views here.

class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'


class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_detail.html'


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'order_create.html'

    def get_success_url(self):
        return reverse('order_detail', kwargs={'pk': self.object.pk})


class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'order_update.html'

    def get_success_url(self):
        return reverse('order_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.order = get_object_or_404(Order, pk=self.kwargs['pk'])
        return super().form_valid(form)


class OrderRejectView(DeleteView):
    model = Order
    template_name = 'order_cancel.html'

    def get_success_url(self):
        return reverse('order_detail', kwargs={'pk': self.object.pk})

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.status = 'canceled'
        self.object.save()
        return HttpResponseRedirect(success_url)


class OrderDeliverView(View):
    def get(self, *args, **kwargs):
        object = get_object_or_404(Order, pk=kwargs['pk'])
        success_url = reverse('order_detail', kwargs={'pk': object.pk})
        if object.status == 'preparing':
            object.status = 'on way'
        elif object.status == 'on way':
            object.status = 'delivered'
        object.save()
        return HttpResponseRedirect(success_url)



class OrderFoodCreateView(CreateView):
    model = OrderFood
    form_class = OrderFoodForm
    template_name = 'order_food_create.html'

    def get_success_url(self):
        return reverse('order_detail', kwargs={'pk': self.object.order.pk})


class OrderFoodUpdateView(UpdateView):
    model = OrderFood
    form_class = OrderFoodForm
    template_name = 'order_food_update.html'

    def get_success_url(self):
        return reverse('order_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.order = get_object_or_404(Order, pk=self.kwargs['pk'])
        return super().form_valid(form)



class OrderFoodDeleteView(DeleteView):
    model = OrderFood


class FoodListView(ListView):
    model = Food
    template_name = 'food_list.html'


class FoodDetailView(DetailView):
    model = Food
    template_name = 'food_detail.html'



class FoodCreateView(CreateView):
    model = Food
    form_class = FoodForm
    template_name = 'food_create.html'


    def get_success_url(self):
        return reverse('food_detail', kwargs={'pk': self.object.pk})




class FoodUpdateView(UpdateView):
    model = Food
    form_class = FoodForm
    template_name = 'food_update.html'

    def get_success_url(self):
        return reverse('food_detail', kwargs={'pk': self.object.pk})
