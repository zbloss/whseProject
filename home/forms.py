from django import forms
from django.forms import ModelForm
from home.models import Incoming, Container, Part


class ContainerForm(ModelForm):
    class Meta:
        model = Container
        fields = ['containerNumber', 'date', 'time']

class PartForm(ModelForm):
    class Meta:
        model = Part
        fields = ['partNumber', 'quantitySkids', 'pcsPerSkid']
