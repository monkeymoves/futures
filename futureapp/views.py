# futureapp/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from tools.models import Pathway, Project, Tool, HorizonScan, Pestle
from tools.forms.project_form import ProjectForm
from django.utils.text import slugify

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
    return render(request, 'tools.html', {'tools': tools})

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
def delphi(request):
    return render(request, 'delphi.html')

@login_required
def seven_questions(request):
    return render(request, 'seven_questions.html')

@login_required
def horizon_scan_tool(request, project_slug):
    """
    Displays the Horizon Scanning page for a specific project.

    Args:
        request: The HTTP request object.
        project_slug: The slug of the project.

    Returns:
        An HTTP response rendering the horizon_scan.html template.
    """
    project = get_object_or_404(Project, slug=project_slug, user=request.user)
    horizon_scan_data = HorizonScan.objects.filter(project=project).first()
    return render(request, 'horizon_scan_tool.html', {'project': project, 'horizon_scan_data': horizon_scan_data})


@login_required
def three_horizons(request):
    return render(request, 'three_horizons.html')

@login_required
def horizon_scanning(request):
    return render(request, 'horizon_scanning.html')


@login_required
def driver_mapping(request):
    return render(request, 'driver_mapping.html')

@login_required
def swot(request):
    return render(request, 'swot.html')

@login_required
def scenarios(request):
    return render(request, 'scenarios.html')

@login_required
def visioning(request):
    return render(request, 'visioning.html')

@login_required
def futures_wheels(request):
    return render(request, 'futures_wheels.html')

@login_required
def policy_stress_testing(request):
    return render(request, 'policy_stress_testing.html')

@login_required
def roadmapping(request):
    return render(request, 'roadmapping.html')

@login_required
def backcasting(request):
    return render(request, 'backcasting.html')

@login_required
def pestle_tool_project(request, project_slug):
    """
    Displays the PESTLE page for a specific project.

    Args:
        request: The HTTP request object.
        project_slug: The slug of the project.

    Returns:
        An HTTP response rendering the pestle.html template.
    """
    project = get_object_or_404(Project, slug=project_slug, user=request.user)
    pestle_data = Pestle.objects.filter(project=project).first()
    return render(request, 'pestle_tool_project.html', {'project': project, 'pestle_data': pestle_data})
