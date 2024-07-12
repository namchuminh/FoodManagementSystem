from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from .forms import UserUpdateForm

def update_user(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thông tin người dùng đã được cập nhật.')
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'user/update_user.html', {'form': form})


def profile(request):
    user = request.user
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')

        if not old_password or not new_password1 or not new_password2:
            messages.error(request, 'Tất cả các trường đều là bắt buộc.')
        elif new_password1 != new_password2:
            messages.error(request, 'Mật khẩu mới và nhập lại mật khẩu không khớp.')
        elif not user.check_password(old_password):
            messages.error(request, 'Mật khẩu cũ không đúng.')
        else:
            user.set_password(new_password1)
            user.save()
            update_session_auth_hash(request, user)  # Giữ người dùng đăng nhập sau khi thay đổi mật khẩu
            messages.success(request, 'Mật khẩu của bạn đã được cập nhật thành công.')
            return redirect('profile')
    
    return render(request, 'user/profile.html', {'user': user})


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