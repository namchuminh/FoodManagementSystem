from django import forms
from .models import Combo
from Food.models import Food

class ComboForm(forms.ModelForm):
    class Meta:
        model = Combo
        fields = ['combo_code', 'combo_name', 'unit_price', 'quantity', 'image', 'products']
        widgets = {
            'products': forms.CheckboxSelectMultiple,
        }
        error_messages = {
            'combo_code': {
                'required': "Mã combo không được để trống.",
                'unique': "Mã combo đã tồn tại.",
            },
            'combo_name': {
                'required': "Tên combo không được để trống.",
            },
            'unit_price': {
                'required': "Đơn giá không được để trống.",
                'invalid': "Đơn giá phải là số nguyên dương.",
            },
            'quantity': {
                'required': "Số lượng không được để trống.",
                'invalid': "Số lượng phải là số nguyên dương.",
            },
            'image': {
                'required': "Hình ảnh không được để trống.",
                'invalid_image': "Định dạng hình ảnh không hợp lệ.",
            },
            'products': {
                'required': "Phải chọn ít nhất một món ăn.",
            },
        }
