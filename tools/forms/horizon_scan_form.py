# tools/forms/horizon_scan_form.py
from django import forms
from tools.models import HorizonScan

class HorizonScanForm(forms.ModelForm):
    class Meta:
        model = HorizonScan
        fields = ['input_data']

    input_data = forms.CharField(widget=forms.Textarea, label='Description of your Horizon Scan')
