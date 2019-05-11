from django.forms import ModelForm, widgets
from django import forms
from apartment.models import Apartment


class ApartmentUpdateForm(ModelForm):
    class Meta:
        model = Apartment
        exclude = ['id', 'created', 'updated']
        widgets = {
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'number': widgets.NumberInput(attrs={'class': 'form-control'}),
            'zip': widgets.NumberInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'rooms': widgets.NumberInput(attrs={'class': 'form-control'}),
            'size': widgets.NumberInput(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'category': widgets.Select(attrs={'class': 'form-control'}),
            'seller': widgets.Select(attrs={'class': 'form-control'}),
            'owner_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'owner_ssn': widgets.NumberInput(attrs={'class': 'form-control'}),
            'owner_phone': widgets.NumberInput(attrs={'class': 'form-control'}),
            'sold': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
        }


class ApartmentAddForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Apartment
        exclude = ['id','created', 'updated','sold']
        widgets = {
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'number': widgets.NumberInput(attrs={'class': 'form-control'}),
            'zip': widgets.Select(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'rooms': widgets.NumberInput(attrs={'class': 'form-control'}),
            'size': widgets.NumberInput(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'category': widgets.Select(attrs={'class': 'form-control'}),
            'seller': widgets.Select(attrs={'class': 'form-control'}),
            'owner_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'owner_ssn': widgets.NumberInput(attrs={'class': 'form-control'}),
            'owner_phone': widgets.NumberInput(attrs={'class': 'form-control'})

        }
