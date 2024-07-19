from django.shortcuts import render
from django.views import View
from Food.models import Food
from Combo.models import Combo
from Coupon.models import Coupon
from Order.models import Order
from django.utils import timezone
from django.db.models import Sum, Count
from datetime import timedelta
from django.http import JsonResponse
import calendar
from django.db.models.functions import ExtractMonth

class Dashboard(View):
    template_name =  'dashboard/index.html'

    def get(self, request):
        # Current date and time
        now = timezone.now()
        start_of_today = now.replace(hour=0, minute=0, second=0, microsecond=0)
        start_of_week = start_of_today - timedelta(days=now.weekday())
        start_of_month = start_of_today.replace(day=1)

        # Revenue and order count for today
        revenue_today = Order.objects.filter(created_at__gte=start_of_today).aggregate(Sum('amount'))['amount__sum'] or 0
        orders_today = Order.objects.filter(created_at__gte=start_of_today).count()

        # Revenue and order count for the current week
        revenue_week = Order.objects.filter(created_at__gte=start_of_week).aggregate(Sum('amount'))['amount__sum'] or 0
        orders_week = Order.objects.filter(created_at__gte=start_of_week).count()

        # Revenue and order count for the current month
        revenue_month = Order.objects.filter(created_at__gte=start_of_month).aggregate(Sum('amount'))['amount__sum'] or 0
        orders_month = Order.objects.filter(created_at__gte=start_of_month).count()

        # Total count of foods, combos, and coupons
        total_foods = Food.objects.count()
        total_combos = Combo.objects.count()
        total_coupons = Coupon.objects.count()

        context = {
            'revenue_today': revenue_today,
            'orders_today': orders_today,
            'revenue_week': revenue_week,
            'orders_week': orders_week,
            'revenue_month': revenue_month,
            'orders_month': orders_month,
            'total_foods': total_foods,
            'total_combos': total_combos,
            'total_coupons': total_coupons,
        }
        return render(request, self.template_name, context)

class RevenueChartView(View):
    def get(self, request):
        # Tạo danh sách chứa doanh thu từ tháng 1 đến tháng 12
        revenue_by_month = [0] * 12
        orders = Order.objects.annotate(month=ExtractMonth('created_at')).values('month').annotate(total_revenue=Sum('amount')).order_by('month')

        for order in orders:
            revenue_by_month[order['month'] - 1] = order['total_revenue']

        return JsonResponse(revenue_by_month, safe=False)
