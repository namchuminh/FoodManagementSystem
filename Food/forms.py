from django import forms
from .models import Food

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['product_code', 'product_name', 'unit_price', 'quantity', 'image']
        error_messages = {
            'product_code': {
                'required': "Mã sản phẩm không được để trống.",
                'unique': "Mã sản phẩm đã tồn tại.",
            },
            'product_name': {
                'required': "Tên sản phẩm không được để trống.",
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
        }

    def clean_unit_price(self):
        unit_price = self.cleaned_data['unit_price']
        if unit_price <= 0:
            raise forms.ValidationError("Đơn giá phải là số nguyên dương.")
        return unit_price

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if quantity <= 0:
            raise forms.ValidationError("Số lượng phải là số nguyên dương.")
        return quantity

    def clean_image(self):
        image = self.cleaned_data['image']
        if not image:
            raise forms.ValidationError("Hình ảnh không được để trống.")
        # Kiểm tra định dạng hình ảnh có thể thêm kiểm tra bằng Pillow
        return image
