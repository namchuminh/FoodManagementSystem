from django import forms
from .models import Order, DetailOrder
from Food.models import Food
from Combo.models import Combo

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

class AddFoodForm(forms.ModelForm):
    class Meta:
        model = DetailOrder
        fields = ['food', 'quantity']
        labels = {
            'food': 'Danh sách đồ ăn',
            'quantity': 'Số lượng',
        }
        error_messages = {
            'food': {
                'required': "Vui lòng chọn món ăn.",
            },
            'quantity': {
                'required': "Vui lòng nhập số lượng.",
                'invalid': "Số lượng phải là số hợp lệ.",
                'min_value': "Số lượng phải lớn hơn 0.",
            },
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['food'].queryset = Food.objects.all()
        self.fields['quantity'].min_value = 1

class AddComboForm(forms.ModelForm):
    class Meta:
        model = DetailOrder
        fields = ['combo', 'quantity']
        labels = {
            'combo': 'Danh sách combo',
            'quantity': 'Số lượng',
        }
        error_messages = {
            'combo': {
                'required': "Vui lòng chọn combo.",
            },
            'quantity': {
                'required': "Vui lòng nhập số lượng.",
                'invalid': "Số lượng phải là số hợp lệ.",
                'min_value': "Số lượng phải lớn hơn 0.",
            },
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['combo'].queryset = Combo.objects.all()
        self.fields['quantity'].min_value = 1