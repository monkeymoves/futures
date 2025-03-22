# tools/forms/pestle_form.py
from django import forms
from tools.models import Project

class PestleForm(forms.Form):
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)
    political = forms.CharField(widget=forms.Textarea, required=False)
    economic = forms.CharField(widget=forms.Textarea, required=False)
    social = forms.CharField(widget=forms.Textarea, required=False)
    technological = forms.CharField(widget=forms.Textarea, required=False)
    legal = forms.CharField(widget=forms.Textarea, required=False)
    environmental = forms.CharField(widget=forms.Textarea, required=False)
    