from django import forms
from django.forms import ModelForm
from home.models import Container, Part


class ContainerForm(ModelForm):
    class Meta:
        model = Container
        fields = ['containerNumber', 'date', 'time', 'part1', 'qty1', 'part2', 'qty2', 'part3', 'qty3', 'part4', 'qty4', 'part5', 'qty5', 'part6', 'qty6', 'part7', 'qty7', 'part8', 'qty8', 'part9', 'qty9', 'part10', 'qty10', 'part11', 'qty11' ]

class PartForm(ModelForm):
    class Meta:
        model = Part
        fields = ['partNumber', 'pcsPerSkid']
