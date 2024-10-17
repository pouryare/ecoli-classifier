from django import forms

class SequenceForm(forms.Form):
    sequence = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}), max_length=1000)