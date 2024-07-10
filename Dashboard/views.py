from django.shortcuts import render
from django.views import View

class Dashboard(View):
    template_name =  'dashboard/index.html'

    def get(self, request):
        data = {
            "title": "Quản trị hệ thống"
        }
        return render(request, self.template_name, data)
    
    def post(self, request):
        pass
