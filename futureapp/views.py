# futureapp/views.py
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from tools.models import Pathway, Project, Tool
from tools.forms.project_form import ProjectForm
from django.contrib.auth import login

def home(request):
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
            project.save()
            return redirect('pathways')  # Redirect to pathway selection (next step)
        else:
            print(form.errors)
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
