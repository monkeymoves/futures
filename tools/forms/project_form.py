# tools/forms/project_form.py
from django import forms
from tools.models import Project, Tool

class ProjectForm(forms.ModelForm):

    tools = forms.ModelMultipleChoiceField(
        queryset=Tool.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    class Meta:
        model = Project
        fields = ['title', 'tools']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tools'].label_from_instance = lambda obj: "%s" % obj.name
