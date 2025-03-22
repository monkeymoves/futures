# tools/urls.py
from django.urls import path
from .views.horizon_scanning import horizon_scanning
from .views.pestle import pestle

urlpatterns = [
    path('horizon-scanning/', horizon_scanning, name='horizon_scanning'),
    path('pestle/', pestle, name='pestle'),
]
