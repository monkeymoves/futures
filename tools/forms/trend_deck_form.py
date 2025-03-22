from django import forms

class TrendDeckForm(forms.Form):
    # This hidden field will hold the JSON string of the selected trend cards.
    scenario_data = forms.CharField(widget=forms.HiddenInput())