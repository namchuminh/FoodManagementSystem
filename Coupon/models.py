from django.db import models

class Coupon(models.Model):
    coupon_code = models.CharField(max_length=100, unique=True, verbose_name="Coupon Code")
    discount_rate = models.PositiveIntegerField(verbose_name="Discount Rate") 
    quantity = models.PositiveIntegerField(verbose_name="Quantity")
    expiration_date = models.DateField(verbose_name="Expiration Date")

    def __str__(self):
        return self.coupon_code