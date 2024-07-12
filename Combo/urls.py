from django.urls import path
from .views import ComboListView, ComboCreateView, ComboUpdateView, ComboDeleteView

urlpatterns = [
    path('', ComboListView.as_view(), name='combo_list'),
    path('add/', ComboCreateView.as_view(), name='combo_create'),
    path('<int:pk>/edit/', ComboUpdateView.as_view(), name='combo_update'),
    path('<int:pk>/delete/', ComboDeleteView.as_view(), name='combo_delete'),
]
