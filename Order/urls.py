from django.urls import path
from .views import OrderListView, OrderCreateView, OrderDeleteView, OrderUpdateView

urlpatterns = [
    path('', OrderListView.as_view(), name='order_list'),
    path('create/', OrderCreateView.as_view(), name='order_create'),
    path('orders/edit/<int:pk>/', OrderUpdateView.as_view(), name='order_edit'),
    path('orders/delete/<int:pk>/', OrderDeleteView.as_view(), name='order_delete'),
]
