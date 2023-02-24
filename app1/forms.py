from django import forms

class SortForm(forms.Form):
    input = forms.CharField(label='Input data')

