# tools/urls.py
from django.urls import path
from .views.horizon_scanning import horizon_scanning
from .views.pestle import pestle
from django.utils.text import slugify

urlpatterns = [
    path('horizon-scanning/', horizon_scanning, name=slugify('Horizon Scanning')),
    path('pestle/', pestle, name=slugify('PESTLE')),
]
