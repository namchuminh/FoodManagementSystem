from django.db import models

class Food(models.Model):
    product_code = models.CharField(max_length=100, unique=True, verbose_name="Product Code")
    product_name = models.CharField(max_length=255, verbose_name="Product Name")
    unit_price = models.PositiveIntegerField(verbose_name="Unit Price")
    quantity = models.PositiveIntegerField(verbose_name="Quantity")
    image = models.ImageField(upload_to='images/', verbose_name="Image")

    def __str__(self):
        return self.product_name
