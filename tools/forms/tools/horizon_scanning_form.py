# core/forms.py
from django import forms

class HorizonScanningForm(forms.Form):
    title = forms.CharField(max_length=100, label='Project Title')
    description = forms.CharField(widget=forms.Textarea, label='Description of your Horizon Scan')