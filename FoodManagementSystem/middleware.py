from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        login_url = reverse('login')
        exempt_urls = [login_url]
        
        if request.user.is_authenticated:
            if request.path in exempt_urls:
                return redirect('dashboard')  # Chuyển hướng tới trang dashboard nếu đã đăng nhập và truy cập trang login/signup
        else:
            if request.path not in exempt_urls:
                return redirect('login')  # Chuyển hướng tới trang login nếu chưa đăng nhập và truy cập trang cần đăng nhập

        response = self.get_response(request)
        return response
