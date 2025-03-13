# tools/forms/horizon_scanning_form.py
from django import forms
from tools.models import Project, HorizonScan

class HorizonScanningForm(forms.ModelForm):
    class Meta:
        model = HorizonScan  # Updated model
        fields = ['input_data']  # Updated fields

    # Remove the user param from the init
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    input_data = forms.CharField(widget=forms.Textarea, label='Description of your Horizon Scan')
