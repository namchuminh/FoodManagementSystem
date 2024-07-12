from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('User.urls')),
    path('', include('Dashboard.urls')),
    path('foods/', include('Food.urls')),
    path('combos/', include('Combo.urls')),
    path('coupon/', include('Coupon.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
