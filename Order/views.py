from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from .models import DetailOrder, Order, Coupon
from .forms import OrderForm, AddComboForm, AddFoodForm
from Food.models import Food
from Combo.models import Combo

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
            messages.success(request, 'Hóa đơn đã được tạo thành công.')
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
            messages.success(request, 'Hóa đơn đã được cập nhật thành công.')
            return redirect('order_list')
        else:
            return render(request, 'orders/order_form.html', {'form': form, 'coupons': coupons})

class OrderDeleteView(View):
    def get(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        order.delete()
        messages.success(request, 'Hóa đơn đã được xóa thành công.')
        return redirect('order_list')

class OrderPaymentView(View):
    def get(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        order.payment = True
        order.save()
        messages.success(request, 'Thanh toán hóa đơn thành công.')
        return redirect('order_list')
    

class OrderMenuView(View):
    def get(self, request, pk):
        order = get_object_or_404(Order, id=pk)
        add_food_form = AddFoodForm()
        add_combo_form = AddComboForm()
        details = DetailOrder.objects.filter(order=order)

        amount = 0

        for detail in details:
            if detail.food:
                detail.total_price = detail.food.unit_price * detail.quantity
            elif detail.combo:
                detail.total_price = detail.combo.unit_price * detail.quantity
            amount = amount + detail.total_price

        if order.coupon:
            discount_amount = amount * (order.coupon.discount_rate / 100)
            amount -= discount_amount
        
        order.amount = int(amount)
        order.save()

        return render(request, 'orders/order_menu.html', {
            'order': order,
            'add_food_form': add_food_form,
            'add_combo_form': add_combo_form,
            'details': details,
            'amount': int(amount)
        })

    def post(self, request, pk):
        order = get_object_or_404(Order, id=pk)
        add_food_form = AddFoodForm()
        add_combo_form = AddComboForm()
        if 'add_food' in request.POST:
            add_food_form = AddFoodForm(request.POST)
            if add_food_form.is_valid():
                detail_order = add_food_form.save(commit=False)
                detail_order.order = order
                detail_order.save()
                messages.success(request, 'Món ăn đã được thêm vào hóa đơn.')
                return redirect('order_menu', pk=order.id)
        elif 'add_combo' in request.POST:
            add_combo_form = AddComboForm(request.POST)
            if add_combo_form.is_valid():
                detail_order = add_combo_form.save(commit=False)
                detail_order.order = order
                detail_order.save()
                messages.success(request, 'Combo đã được thêm vào hóa đơn.')
                return redirect('order_menu', pk=order.id)
        else:
            add_food_form = AddFoodForm()
            add_combo_form = AddComboForm()
        
        return render(request, 'orders/order_menu.html', {
            'order': order,
            'add_food_form': add_food_form,
            'add_combo_form': add_combo_form,
        })
