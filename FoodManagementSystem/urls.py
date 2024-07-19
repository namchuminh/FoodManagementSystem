from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('User.urls')),
    path('', include('Dashboard.urls'), name='dashboard'),
    path('foods/', include('Food.urls')),
    path('combos/', include('Combo.urls')),
    path('coupon/', include('Coupon.urls')),
    path('orders/', include('Order.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
