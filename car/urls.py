from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.show_cars, name='home'),
    path('details/<int:id>/', views.CarDetail.as_view(), name='detail'),
    path('sort_brand/<int:id>/', views.sort_brand, name='sort_brand'),
    path('buy_car/<int:id>/', views.buy_car, name='buy_car')
]

if settings.DEBUG:
    urlpatterns += static( settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
