# tools/views/pestle.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from tools.models import Project, Pathway, Tool, Pestle, UserInput
from tools.forms.pestle_form import PestleForm
from django.http import Http404

@login_required
def pestle(request):
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
        form = PestleForm(request.POST)
        if form.is_valid():

            pestle_analysis = form.save(commit=False) #do not save yet.
            pestle_analysis.project = project #set the project
            pestle_analysis.save() #now we can save.

            # Get or create a pathway for 'Strategic Analysis'
            pathway, created = Pathway.objects.get_or_create(
                name='Strategic Analysis',
                defaults={'description': 'Pathway for strategic analysis tools'}
            )

            # Get or create the PESTLE tool and link it to the pathway
            pestle_tool, created = Tool.objects.get_or_create(
                name='PESTLE',
                defaults={
                    'description': 'PESTLE tool description',
                }
            )
            # Associate the tool with the pathway
            pestle_tool.pathways.add(pathway)

            user_input, created = UserInput.objects.get_or_create(
                project=project,
                tool=pestle_tool
            )

            user_input.pestle = pestle_analysis
            user_input.save()

            return redirect('home')  # Redirect after PESTLE analysis
        else:
            print(form.errors)
    else:
        form = PestleForm()

    return render(request, 'tools/pestle.html', {'form': form})
