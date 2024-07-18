from django.db import models
import string
import random
from django.utils import timezone
from Coupon.models import Coupon
from Combo.models import Combo
from Food.models import Food

def generate_random_code(length=10):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

class Order(models.Model):
    code = models.CharField(max_length=10, unique=True, default=generate_random_code, verbose_name="Order Code")
    customer = models.CharField(max_length=255, verbose_name="Customer Name")
    phone = models.CharField(max_length=15, verbose_name="Phone Number", null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    coupon = models.ForeignKey(Coupon, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Coupon Code")
    note = models.TextField(default=None, null=True, blank=True)
    amount = models.PositiveIntegerField(verbose_name="Amount", default=0)
    payment = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return f"Order {self.code} by {self.customer}"


class DetailOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Order")
    food = models.ForeignKey(Food, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Food")
    combo = models.ForeignKey(Combo, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Combo")
    quantity = models.PositiveIntegerField(verbose_name="Quantity")

    def __str__(self):
        return f"Detail of {self.order.code}"