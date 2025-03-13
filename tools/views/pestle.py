# tools/views/pestle.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from tools.models import Project, Pathway, Tool, Pestle, UserInput
from tools.forms.pestle_form import PestleForm

@login_required
def pestle(request):
    if request.method == 'POST':
        form = PestleForm(request.POST)
        if form.is_valid():
            # Get the currently selected project from the session
            project = Project.objects.first() # this will be replaced with the project session.

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

