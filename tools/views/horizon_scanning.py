# # tools/views.py
# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from models import Tool, Pathway
# from forms.tools import HorizonScanningForm  # you can also move the form into tools/forms.py

# tools/views/horizon_scanning.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from tools.models import Tool, Pathway  # Corrected import
from tools.forms.tools.horizon_scanning_form import HorizonScanningForm # Correct import

@login_required
def horizon_scanning(request):
    if request.method == 'POST':
        form = HorizonScanningForm(request.POST)
        if form.is_valid():
            # create a Tool or find it, link to Pathways, etc.
            ...
            return redirect('home')
    else:
        form = HorizonScanningForm()

    return render(request, 'tools/horizon_scanning.html', {'form': form})


@login_required
def horizon_scanning(request):
    if request.method == 'POST':
        form = HorizonScanningForm(request.POST)
        if form.is_valid():
            # create a Tool or find it, link to Pathways, etc.
            ...
            return redirect('home')
    else:
        form = HorizonScanningForm()

    return render(request, 'tools/horizon_scanning.html', {'form': form})