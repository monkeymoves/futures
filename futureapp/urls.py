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
    path('projects/<slug:project_slug>/tools/delphi/', views.delphi, name='delphi'),
    path('projects/<slug:project_slug>/tools/seven-questions/', views.seven_questions, name='seven_questions'),
    path('projects/<slug:project_slug>/tools/horizon-scanning/', views.horizon_scanning, name='horizon_scanning'),
    path('projects/<slug:project_slug>/tools/three-horizons/', views.three_horizons, name='three_horizons'),
    path('projects/<slug:project_slug>/tools/driver-mapping/', views.driver_mapping, name='driver_mapping'),
    path('projects/<slug:project_slug>/tools/swot/', views.swot, name='swot'),
    path('projects/<slug:project_slug>/tools/scenarios/', views.scenarios, name='scenarios'),
    path('projects/<slug:project_slug>/tools/visioning/', views.visioning, name='visioning'),
    path('projects/<slug:project_slug>/tools/futures-wheels/', views.futures_wheels, name='futures_wheels'),
    path('projects/<slug:project_slug>/tools/policy-stress-testing/', views.policy_stress_testing, name='policy_stress_testing'),
    path('projects/<slug:project_slug>/tools/roadmapping/', views.roadmapping, name='roadmapping'),
    path('projects/<slug:project_slug>/tools/backcasting/', views.backcasting, name='backcasting'),
    path('projects/<slug:project_slug>/tools/pestle/', views.pestle, name='pestle'),
    path('projects/<slug:project_slug>/', views.project_detail, name='project_detail'),
]
