# tools/urls.py
from django.urls import path
from .views.horizon_scanning import horizon_scanning
from django.utils.text import slugify

urlpatterns = [
    path('horizon-scanning/', horizon_scanning, name=slugify('Horizon Scanning')),
]
