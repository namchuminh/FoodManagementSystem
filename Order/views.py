from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from .models import Order, Coupon
from .forms import OrderForm

class OrderListView(View):
    def get(self, request):
        orders = Order.objects.all().order_by('-created_at')
        return render(request, 'orders/order_list.html', {'orders': orders})

class OrderCreateView(View):
    def get(self, request):
        form = OrderForm()
        coupons = Coupon.objects.all()
        return render(request, 'orders/order_form.html', {'form': form, 'coupons': coupons})

    def post(self, request):
        form = OrderForm(request.POST)
        coupons = Coupon.objects.all()
        if form.is_valid():
            form.save()
            messages.success(request, 'Đơn hàng đã được tạo thành công.')
            return redirect('order_list')
        else:
            return render(request, 'orders/order_form.html', {'form': form, 'coupons': coupons})

class OrderUpdateView(View):
    def get(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        form = OrderForm(instance=order)
        coupons = Coupon.objects.all()
        return render(request, 'orders/order_form.html', {'form': form, 'coupons': coupons})

    def post(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        form = OrderForm(request.POST, instance=order)
        coupons = Coupon.objects.all()
        if form.is_valid():
            form.save()
            messages.success(request, 'Đơn hàng đã được cập nhật thành công.')
            return redirect('order_list')
        else:
            return render(request, 'orders/order_form.html', {'form': form, 'coupons': coupons})

class OrderDeleteView(View):
    def get(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        order.delete()
        messages.success(request, 'Đơn hàng đã được xóa thành công.')
        return redirect('order_list')
