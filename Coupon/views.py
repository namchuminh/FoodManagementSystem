from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.views import View
from .models import Coupon
from .forms import CouponForm

class CouponListView(View):
    def get(self, request):
        coupons = Coupon.objects.all()
        return render(request, 'coupons/coupon_list.html', {'coupons': coupons})

class CouponCreateView(View):
    def get(self, request):
        form = CouponForm()
        return render(request, 'coupons/coupon_form.html', {'form': form, 'title': 'Thêm Mã Giảm Giá'})

    def post(self, request):
        form = CouponForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mã giảm giá đã được thêm thành công.')
            return redirect('coupon_list')
        return render(request, 'coupons/coupon_form.html', {'form': form, 'title': 'Thêm Mã Giảm Giá'})

class CouponUpdateView(View):
    def get(self, request, pk):
        coupon = get_object_or_404(Coupon, pk=pk)
        form = CouponForm(instance=coupon)
        return render(request, 'coupons/coupon_form.html', {'form': form, 'title': 'Sửa Mã Giảm Giá'})

    def post(self, request, pk):
        coupon = get_object_or_404(Coupon, pk=pk)
        form = CouponForm(request.POST, instance=coupon)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mã giảm giá đã được cập nhật thành công.')
            return redirect('coupon_list')
        return render(request, 'coupons/coupon_form.html', {'form': form, 'title': 'Sửa Mã Giảm Giá'})

class CouponDeleteView(View):
    def get(self, request, pk):
        coupon = get_object_or_404(Coupon, pk=pk)
        coupon.delete()
        messages.success(request, 'Mã giảm giá đã được xóa thành công.')
        return redirect('coupon_list')
