# tools/forms/pestle_form.py
from django import forms
from tools.models import Pestle

class PestleForm(forms.ModelForm):
    class Meta:
        model = Pestle
        fields = ['political', 'economic', 'social', 'technological', 'legal', 'environmental']
        widgets = {
            'political': forms.Textarea(attrs={'rows': 4}),
            'economic': forms.Textarea(attrs={'rows': 4}),
            'social': forms.Textarea(attrs={'rows': 4}),
            'technological': forms.Textarea(attrs={'rows': 4}),
            'legal': forms.Textarea(attrs={'rows': 4}),
            'environmental': forms.Textarea(attrs={'rows': 4}),
        }
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # Remove project form - this should be done in the views
