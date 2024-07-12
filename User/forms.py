from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.translation import gettext_lazy as _

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
        error_messages = {
            'first_name': {
                'required': "Họ đệm không được để trống.",
            },
            'last_name': {
                'required': "Tên không được để trống.",
            },
            'username': {
                'required': "Tài khoản không được để trống.",
                'unique': "Tài khoản đã tồn tại.",
            },
            'email': {
                'required': "Email không được để trống.",
                'invalid': "Email không hợp lệ.",
            },
        }

