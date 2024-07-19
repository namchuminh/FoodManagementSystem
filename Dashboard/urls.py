from django.urls import path
from .views import Dashboard, RevenueChartView

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
    path('revenue-data/', RevenueChartView.as_view(), name='revenue_data'),
    path('dashboard/', Dashboard.as_view(), name='dashboard')
]