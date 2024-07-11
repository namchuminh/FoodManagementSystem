# myapp/urls.py
from django.urls import path
from .views import FoodListView, FoodCreateView, FoodUpdateView, FoodDeleteView

urlpatterns = [
    path('', FoodListView.as_view(), name='food_list'),
    path('add/', FoodCreateView.as_view(), name='food_add'),
    path('<int:pk>/edit/', FoodUpdateView.as_view(), name='food_edit'),
    path('<int:pk>/delete/', FoodDeleteView.as_view(), name='food_delete'),
]
