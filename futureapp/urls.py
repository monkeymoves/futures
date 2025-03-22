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
    path("tools/", views.tools, name="tools"),
    # New tool URLs (outside of project context)
    path('tools/delphi/', views.delphi, name='delphi'),
    path('tools/seven-questions/', views.seven_questions, name='seven_questions'),
    path('tools/three-horizons/', views.three_horizons, name='three_horizons'),
    path('tools/driver-mapping/', views.driver_mapping, name='driver_mapping'),
    path('tools/swot/', views.swot, name='swot'),
    path('tools/scenarios/', views.scenarios, name='scenarios'),
    path('tools/visioning/', views.visioning, name='visioning'),
    path('tools/futures-wheels/', views.futures_wheels, name='futures_wheels'),
    path('tools/policy-stress-testing/', views.policy_stress_testing, name='policy_stress_testing'),
    path('tools/roadmapping/', views.roadmapping, name='roadmapping'),
    path('tools/backcasting/', views.backcasting, name='backcasting'),
    path('tools/pestle/', views.pestle, name='pestle'),
    path('tools/horizon-scanning/', views.horizon_scanning, name='horizon_scanning'),
    # Existing tool URLs (within project context)
    path('projects/<slug:project_slug>/tools/delphi/', views.delphi, name='project_delphi'),
    path('projects/<slug:project_slug>/tools/seven-questions/', views.seven_questions, name='project_seven_questions'),
    path('projects/<slug:project_slug>/tools/three-horizons/', views.three_horizons, name='project_three_horizons'),
    path('projects/<slug:project_slug>/tools/driver-mapping/', views.driver_mapping, name='project_driver_mapping'),
    path('projects/<slug:project_slug>/tools/swot/', views.swot, name='project_swot'),
    path('projects/<slug:project_slug>/tools/scenarios/', views.scenarios, name='project_scenarios'),
    path('projects/<slug:project_slug>/tools/visioning/', views.visioning, name='project_visioning'),
    path('projects/<slug:project_slug>/tools/futures-wheels/', views.futures_wheels, name='project_futures_wheels'),
    path('projects/<slug:project_slug>/tools/policy-stress-testing/', views.policy_stress_testing, name='project_policy_stress_testing'),
    path('projects/<slug:project_slug>/tools/roadmapping/', views.roadmapping, name='project_roadmapping'),
    path('projects/<slug:project_slug>/tools/backcasting/', views.backcasting, name='project_backcasting'),
    path('projects/<slug:project_slug>/tools/pestle/', views.pestle, name='project_pestle'),
    path('projects/<slug:project_slug>/tools/horizon-scanning/', views.horizon_scanning, name='project_horizon_scanning'),
    path('projects/<slug:project_slug>/', views.project_detail, name='project_detail'),
    path('tools/trend_deck/', views.trend_deck, name='trend_deck'),
    # Optional: If you want to pass a project slug via the URL
    path('tools/trend_deck/<slug:project_slug>/', views.trend_deck, name='trend_deck_project'),
]
