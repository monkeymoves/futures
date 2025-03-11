# tools/views/horizon_scanning.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from tools.models import Tool, Pathway, Project, UserInput
from tools.forms.horizon_scanning_form import HorizonScanningForm

@login_required
def horizon_scanning(request):
    if request.method == 'POST':
        form = HorizonScanningForm(request.user, request.POST)
        if form.is_valid():
            user_input = form.save(commit=False)  # Create UserInput object but don't save yet
            project = form.cleaned_data['project'] # retrieve the project that has been selected.

            # Get or create a pathway for 'Strategic Analysis'
            pathway, created = Pathway.objects.get_or_create(
                name='Strategic Analysis',
                defaults={'description': 'Pathway for strategic analysis tools'}
            )

            # Get or create the Horizon Scanning tool and link it to the pathway
            horizon_tool, created = Tool.objects.get_or_create(
                name='Horizon Scanning',
                defaults={
                    'description': 'Horizon Scanning tool description',
                }
            )
            # Associate the tool with the pathway
            horizon_tool.pathways.add(pathway)

            user_input.tool = horizon_tool
            user_input.save()

            return redirect('home')
        else:
            print(form.errors)
    else:
        form = HorizonScanningForm(request.user)

    return render(request, 'tools/horizon_scanning.html', {'form': form})
