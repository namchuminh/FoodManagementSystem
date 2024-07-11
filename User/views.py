from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.utils.translation import gettext_lazy as _

class Login(View):
    template_name =  'user/login.html'

    def get(self, request):
        data = {
            "title": "Đăng nhập hệ thống"
        }
        return render(request, self.template_name, data)
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        errors = {}

        if not username:
            errors['username'] = _('Tài khoản không được để trống')
        
        if not password:
            errors['password'] = _('Mật khẩu không được để trống')
        
        if not errors:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Chuyển hướng đến trang chủ hoặc trang mong muốn
            else:
                errors['non_field'] = _('Tài khoản hoặc mật khẩu không đúng')

        data = {
            "title": "Đăng nhập hệ thống",
            "errors": errors,
            "password": password,
        }
        return render(request, self.template_name, data)

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('login')