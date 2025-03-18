# tools/forms/project_form.py
from django import forms
from tools.models import Project, Pathway, Tool

class ProjectForm(forms.ModelForm):
    pathways = forms.ModelMultipleChoiceField(
        queryset=Pathway.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    tools = forms.ModelMultipleChoiceField(
        queryset=Tool.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    class Meta:
        model = Project
        fields = ['title', 'pathways', 'tools']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pathways'].label_from_instance = lambda obj: "%s" % obj.name
        self.fields['tools'].label_from_instance = lambda obj: "%s" % obj.name
