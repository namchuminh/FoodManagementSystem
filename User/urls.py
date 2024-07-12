from django.urls import path
from .views import Login, Logout, update_user, profile

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('update_user/', update_user, name='update_user'),
    path('profile/', profile, name='profile'),
]