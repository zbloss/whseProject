from django import forms

class IncomingForm(forms.Form):
    name = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea)
