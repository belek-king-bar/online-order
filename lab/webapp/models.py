from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='info', verbose_name='Пользователи системы')
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name='Телефон')


class Food(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название блюда')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    photo = models.ImageField(verbose_name='Фотография')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')

class Order(models.Model):
    STATUS_NEW = 'new'
    STATUS_PREPARING = 'preparing'
    STATUS_ON_WAY = 'on way'
    STATUS_DELIVERED = 'delivered'
    STATUS_CANCELED = 'canceled'

    STATUS_CHOICES = (
        (STATUS_NEW, 'Новый'),
        (STATUS_PREPARING, 'Готовится'),
        (STATUS_ON_WAY, 'В пути'),
        (STATUS_DELIVERED, 'Доставлен'),
        (STATUS_CANCELED, 'Отменен')
    )

    contact_phone = models.CharField(max_length=20, null=True, blank=True, verbose_name='Телефон')
    contact_name = models.CharField(max_length=50, verbose_name='Имя клиента')
    delivery_address = models.CharField(max_length=200, verbose_name='Адрес')
    status = models.CharField(max_length=20, default=STATUS_NEW, verbose_name='Статус', choices=STATUS_CHOICES)
    operator = models.ForeignKey(User, related_name='orders', null=True, blank=True, verbose_name='Оператор', on_delete=models.PROTECT)
    courier = models.ForeignKey(User, related_name='delivered', null=True, blank=True, verbose_name='Курьер', on_delete=models.PROTECT)




class OrderFood(models.Model):
    order = models.ForeignKey(Order, related_name='foods', verbose_name='Заказ', on_delete=models.PROTECT)
    food = models.ForeignKey(Food, related_name='+', verbose_name='Блюдо', on_delete=models.PROTECT)
    amount = models.IntegerField(verbose_name='Количество')