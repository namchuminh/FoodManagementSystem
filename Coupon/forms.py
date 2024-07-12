from django import forms
from .models import Coupon

class CouponForm(forms.ModelForm):
    class Meta:
        model = Coupon
        fields = ['coupon_code', 'discount_rate', 'quantity', 'expiration_date']
        error_messages = {
            'coupon_code': {
                'required': "Mã giảm giá không được để trống.",
                'unique': "Mã giảm giá đã tồn tại.",
            },
            'discount_rate': {
                'required': "Tỷ lệ giảm không được để trống.",
                'invalid': "Tỷ lệ giảm phải là số nguyên dương.",
            },
            'quantity': {
                'required': "Số lượng không được để trống.",
                'invalid': "Số lượng phải là số nguyên dương.",
            },
            'expiration_date': {
                'required': "Ngày hết hạn không được để trống.",
                'invalid': "Ngày hết hạn không hợp lệ.",
            },
        }
