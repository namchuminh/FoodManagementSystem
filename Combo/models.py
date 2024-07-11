from django.db import models
from Food.models import Food

class Combo(models.Model):
    combo_code = models.CharField(max_length=100, unique=True, verbose_name="Combo Code")
    combo_name = models.CharField(max_length=255, verbose_name="Combo Name")
    unit_price = models.PositiveIntegerField(verbose_name="Unit Price")
    quantity = models.PositiveIntegerField(verbose_name="Quantity")
    image = models.ImageField(upload_to='images/', verbose_name="Image")
    products = models.ManyToManyField(Food, related_name='combos', verbose_name="Products")

    def __str__(self):
        return self.combo_name
