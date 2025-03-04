from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import HorizonScanningForm
from .models import Project, Tool, UserInput, Pathway

# @login_required
# def horizon_scanning(request):
#     if request.method == 'POST':
#         form = HorizonScanningForm(request.POST)
#         if form.is_valid():
#             project = Project.objects.create(user=request.user, title=form.cleaned_data['title'])

#             # Explicitly create or get the pathway right here:
#             pathway, created = Pathway.objects.get_or_create(
#                 name='Strategic Analysis',
#                 defaults={'description': 'Pathway for strategic analysis tools'}
#             )

#             # Clearly link the Tool to the Pathway immediately:
#             horizon_tool, created = Tool.objects.get_or_create(
#                 name='Horizon Scanning',
#                 defaults={
#                     'description': 'Horizon Scanning tool description',
#                     'pathway': pathway  # explicitly link pathway here!
#                 }
#             )

#             # Now save the user input associated with the project:
#             UserInput.objects.create(
#                 project=project,
#                 tool=horizon_tool,
#                 input_data={'description': form.cleaned_data['description']}
#             )

#             return redirect('home')
#     else:
#         form = HorizonScanningForm()

#     return render(request, 'core/horizon_scanning.html', {'form': form})

def home(request):
    return HttpResponse('Welcome')