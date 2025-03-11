# tools/forms/project_form.py
from django import forms
from tools.models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title']
