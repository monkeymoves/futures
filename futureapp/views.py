# futureapp/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from tools.models import Pathway, Project, Tool, HorizonScan, Pestle
from tools.forms.project_form import ProjectForm
from tools.forms.horizon_scan_form import HorizonScanForm
from tools.forms.pestle_form import PestleForm
from django.utils.text import slugify
from tools.forms.delphi_form import DelphiForm
from tools.forms.seven_questions_form import SevenQuestionsForm
from tools.forms.three_horizons_form import ThreeHorizonsForm
from tools.forms.driver_mapping_form import DriverMappingForm
from tools.forms.swot_form import SwotForm
from tools.forms.scenarios_form import ScenariosForm
from tools.forms.visioning_form import VisioningForm
from tools.forms.futures_wheels_form import FuturesWheelsForm
from tools.forms.policy_stress_testing_form import PolicyStressTestingForm
from tools.forms.roadmapping_form import RoadmappingForm
from tools.forms.backcasting_form import BackcastingForm


def home(request):
    # Check if the user is logged in
    if request.user.is_authenticated:
        # Get the user's projects
        projects = Project.objects.filter(user=request.user)
        # Pass the projects to the template
        return render(request, 'home.html', {'projects': projects})
    else:
        # User is not logged in, render the default home page
        return render(request, 'home.html')


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

@login_required
def projects(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.slug = slugify(project.title)
            project.save()
            form.save_m2m()
            return redirect('project_detail', project_slug=project.slug)
        else:
            # Pass the errors to the template
            projects = Project.objects.filter(user=request.user)
            return render(request, 'projects.html', {'form': form, 'projects': projects, 'errors': form.errors})
    else:
        form = ProjectForm()

    projects = Project.objects.filter(user=request.user)
    return render(request, 'projects.html', {'form': form, 'projects': projects})

@login_required
def pathways(request):
    pathways = Pathway.objects.all()
    return render(request, 'pathways.html', {'pathways': pathways})

@login_required
def tools(request):
    tools = Tool.objects.all()
    project_slug = request.GET.get('project_slug')
    project = None
    if project_slug:
        project = get_object_or_404(Project, slug=project_slug, user=request.user)
    return render(request, 'tools.html', {'tools': tools, 'project': project, 'project_slug': project_slug})

@login_required
def project_detail(request, project_slug):
    """
    Displays the details of a specific project.

    Args:
        request: The HTTP request object.
        project_slug: The slug of the project to display.

    Returns:
        An HTTP response rendering the project_detail.html template.
    """
    project = get_object_or_404(Project, slug=project_slug, user=request.user)
    return render(request, 'project_detail.html', {'project': project})

@login_required
def horizon_scanning(request, project_slug=None):
    project = None
    if project_slug:
        project = get_object_or_404(Project, slug=project_slug, user=request.user)

    if request.method == 'POST':
        form = HorizonScanForm(request.POST)
        if form.is_valid():
            horizon_scan = form.save(commit=False)
            if project:
                horizon_scan.project = project
            horizon_scan.save()
            if project:
                return redirect('project_detail', project_slug=project.slug)
    else:
        form = HorizonScanForm()
    return render(request, 'horizon_scanning.html', {'form': form, 'project':project})

@login_required
def pestle(request, project_slug=None):
    project = None
    if project_slug:
        project = get_object_or_404(Project, slug=project_slug, user=request.user)
    if request.method == 'POST':
        form = PestleForm(request.POST)
        if form.is_valid():
            pestle = form.save(commit=False)
            if project:
                pestle.project = project
            pestle.save()
            if project:
                return redirect('project_detail', project_slug=project.slug)
    else:
        form = PestleForm()
    return render(request, 'pestle.html', {'form': form, 'project':project})

@login_required
def delphi(request, project_slug=None):
    project = None
    if project_slug:
        project = get_object_or_404(Project, slug=project_slug, user=request.user)
    form = DelphiForm()
    return render(request, 'delphi.html', {'form': form, 'project': project})

@login_required
def seven_questions(request, project_slug=None):
    project = None
    if project_slug:
        project = get_object_or_404(Project, slug=project_slug, user=request.user)
    form = SevenQuestionsForm()
    return render(request, 'seven_questions.html', {'form': form, 'project': project})

@login_required
def three_horizons(request, project_slug=None):
    project = None
    if project_slug:
        project = get_object_or_404(Project, slug=project_slug, user=request.user)
    form = ThreeHorizonsForm()
    return render(request, 'three_horizons.html', {'form': form, 'project': project})

@login_required
def driver_mapping(request, project_slug=None):
    project = None
    if project_slug:
        project = get_object_or_404(Project, slug=project_slug, user=request.user)
    form = DriverMappingForm()
    return render(request, 'driver_mapping.html', {'form': form, 'project': project})

@login_required
def swot(request, project_slug=None):
    project = None
    if project_slug:
        project = get_object_or_404(Project, slug=project_slug, user=request.user)
    form = SwotForm()
    return render(request, 'swot.html', {'form': form, 'project': project})

@login_required
def scenarios(request, project_slug=None):
    project = None
    if project_slug:
        project = get_object_or_404(Project, slug=project_slug, user=request.user)
    form = ScenariosForm()
    return render(request, 'scenarios.html', {'form': form, 'project': project})

@login_required
def visioning(request, project_slug=None):
    project = None
    if project_slug:
        project = get_object_or_404(Project, slug=project_slug, user=request.user)
    form = VisioningForm()
    return render(request, 'visioning.html', {'form': form, 'project': project})

@login_required
def futures_wheels(request, project_slug=None):
    project = None
    if project_slug:
        project = get_object_or_404(Project, slug=project_slug, user=request.user)
    form = FuturesWheelsForm()
    return render(request, 'futures_wheels.html', {'form': form, 'project': project})

@login_required
def policy_stress_testing(request, project_slug=None):
    project = None
    if project_slug:
        project = get_object_or_404(Project, slug=project_slug, user=request.user)
    form = PolicyStressTestingForm()
    return render(request, 'policy_stress_testing.html', {'form': form, 'project': project})

@login_required
def roadmapping(request, project_slug=None):
    project = None
    if project_slug:
        project = get_object_or_404(Project, slug=project_slug, user=request.user)
    form = RoadmappingForm()
    return render(request, 'roadmapping.html', {'form': form, 'project': project})

@login_required
def backcasting(request, project_slug=None):
    project = None
    if project_slug:
        project = get_object_or_404(Project, slug=project_slug, user=request.user)
    form = BackcastingForm()
    return render(request, 'backcasting.html', {'form': form, 'project': project})
