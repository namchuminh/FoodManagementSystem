from django.urls import path
from .views import CouponListView, CouponCreateView, CouponUpdateView, CouponDeleteView

urlpatterns = [
    path('', CouponListView.as_view(), name='coupon_list'),
    path('add/', CouponCreateView.as_view(), name='coupon_create'),
    path('<int:pk>/edit/', CouponUpdateView.as_view(), name='coupon_update'),
    path('<int:pk>/delete/', CouponDeleteView.as_view(), name='coupon_delete'),
]