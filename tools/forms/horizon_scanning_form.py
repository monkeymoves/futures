# tools/forms/horizon_scanning_form.py
from django import forms
from tools.models import Project, UserInput

class HorizonScanningForm(forms.ModelForm):
    class Meta:
        model = UserInput
        fields = ['project', 'input_data']

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if user.is_authenticated:
            self.fields['project'].queryset = Project.objects.filter(user=user)
        self.fields['input_data'].widget = forms.Textarea()

    project = forms.ModelChoiceField(
        queryset=Project.objects.none(),  # Start with an empty queryset
        label='Select Project',
        required=True,
    )
    input_data = forms.CharField(widget=forms.Textarea, label='Description of your Horizon Scan')
