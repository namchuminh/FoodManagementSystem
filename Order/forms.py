from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'phone', 'coupon', 'note']
        error_messages = {
            'customer': {
                'required': "Tên khách hàng không được để trống.",
            },
            'phone': {
                'required': "Số điện thoại không được để trống.",
                'invalid': "Số điện thoại không hợp lệ.",
            },
            'coupon': {
                'invalid': "Mã giảm giá không hợp lệ.",
            },
        }

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['customer'].label = "Tên khách hàng"
        self.fields['phone'].label = "Số điện thoại"
        self.fields['coupon'].label = "Mã giảm giá"
        self.fields['note'].label = "Ghi chú"
        self.fields['coupon'].required = False
