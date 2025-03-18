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
    path('tools/delphi/', views.delphi, name='delphi'),
    path('tools/seven-questions/', views.seven_questions, name='seven_questions'),
    path('tools/horizon-scanning/', views.horizon_scanning, name='horizon_scanning'),
    path('tools/three-horizons/', views.three_horizons, name='three_horizons'),
    path('tools/driver-mapping/', views.driver_mapping, name='driver_mapping'),
    path('tools/swot/', views.swot, name='swot'),
    path('tools/scenarios/', views.scenarios, name='scenarios'),
    path('tools/visioning/', views.visioning, name='visioning'),
    path('tools/futures-wheels/', views.futures_wheels, name='futures_wheels'),
    path('tools/policy-stress-testing/', views.policy_stress_testing, name='policy_stress_testing'),
    path('tools/roadmapping/', views.roadmapping, name='roadmapping'),
    path('tools/backcasting/', views.backcasting, name='backcasting'),
    path('tools/pestle/', views.pestle_tool_project, name='pestle_tool'),
    path('projects/<slug:project_slug>/', views.project_detail, name='project_detail'),
    path('projects/<slug:project_slug>/horizon-scan/', views.horizon_scan_tool, name='horizon_scan_tool'),
    path('projects/<slug:project_slug>/pestle/', views.pestle_tool_project, name='pestle_tool_project'),
]
