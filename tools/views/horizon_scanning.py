# tools/views/horizon_scanning.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from tools.models import Tool, Pathway, Project, UserInput, HorizonScan
from tools.forms.horizon_scanning_form import HorizonScanningForm

@login_required
def horizon_scanning(request):
    if request.method == 'POST':
        # remove the user argument
        form = HorizonScanningForm(request.POST)
        if form.is_valid():
            #get project
            project = Project.objects.first() # this will be changed to use sessions.

            horizon_scan = form.save()
            horizon_scan.project = project
            horizon_scan.save()

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

            user_input, created = UserInput.objects.get_or_create(
                project=project,
                tool=horizon_tool
            )
            user_input.horizonscan = horizon_scan
            user_input.save()

            return redirect('home')
        else:
            print(form.errors)
    else:
        # remove the user argument
        form = HorizonScanningForm()

    return render(request, 'tools/horizon_scanning.html', {'form': form})
