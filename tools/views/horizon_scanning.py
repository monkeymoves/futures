# tools/views/horizon_scanning.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from tools.models import Tool, Pathway, Project, UserInput, HorizonScan
from tools.forms.horizon_scanning_form import HorizonScanningForm
from django.http import Http404

@login_required
def horizon_scanning(request):
    # Get the project ID from the session
    project_id = request.session.get('project_id')

    # If there's no project ID in the session, raise a 404 error
    if not project_id:
        raise Http404("No project selected.")

    # Retrieve the project
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        raise Http404("Project does not exist.")

    if request.method == 'POST':
        # remove the user argument
        form = HorizonScanningForm(request.POST)
        if form.is_valid():
            horizon_scan = form.save(commit=False)
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
