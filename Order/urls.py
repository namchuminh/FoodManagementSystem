from django.urls import path
from .views import OrderListView, OrderCreateView, OrderDeleteView, OrderUpdateView, OrderPaymentView, OrderMenuView

urlpatterns = [
    path('', OrderListView.as_view(), name='order_list'),
    path('create/', OrderCreateView.as_view(), name='order_create'),
    path('orders/edit/<int:pk>/', OrderUpdateView.as_view(), name='order_edit'),
    path('orders/delete/<int:pk>/', OrderDeleteView.as_view(), name='order_delete'),
    path('orders/payment/<int:pk>/', OrderPaymentView.as_view(), name='order_payment'),
    path('orders/menu/<int:pk>/', OrderMenuView.as_view(), name='order_menu'),
]
