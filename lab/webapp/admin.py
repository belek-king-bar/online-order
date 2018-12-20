from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from webapp.models import Employee, Food, Order, OrderFood

# Register your models here.
class EmployeeInline(admin.StackedInline):
    model = Employee
    fields = ['phone']

class EmployeeAdmin(UserAdmin):
    inlines = [EmployeeInline]

class OrderFoodInline(admin.TabularInline):
    model = OrderFood

class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [OrderFoodInline]

admin.site.unregister(User)
admin.site.register(User, EmployeeAdmin)
admin.site.register(Food)
admin.site.register(Order, OrderAdmin)