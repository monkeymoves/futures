# futureapp/urls.py
from django.contrib import admin
from django.urls import include, path
from . import views  # Import from .views (futureapp.views)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Use views.home
    path('', include('django.contrib.auth.urls')),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path("projects/", views.projects, name="projects"),
    path("pathways/", views.pathways, name="pathways"),
    path("tools/", views.tools, name="tools"),
    path("", include('tools.urls')),
]
