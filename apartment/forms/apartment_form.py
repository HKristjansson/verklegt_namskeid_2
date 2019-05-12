from django.forms import ModelForm, widgets, forms
from django import forms
from apartment.models import Apartment
from urllib import request


class ApartmentBuyForm(forms.ModelForm):
    class Meta:
        model = Apartment
        exclude = ['id', 'created', 'updated', 'sold']
        readonly_fields = ['address', 'number', 'zip', 'description', 'rooms', 'size', 'price', 'category',
                           'seller', 'owner_name', 'owner_ssn', 'owner_phone']
        widgets = {
            'address': widgets.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'number': widgets.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'zip': widgets.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'description': widgets.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'rooms': widgets.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'size': widgets.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'price': widgets.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'category': widgets.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'seller': widgets.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'owner_name': widgets.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'owner_ssn': widgets.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'owner_phone': widgets.TextInput(attrs={'class': 'form-control', 'readonly': True})

        }
        # else:
        #     widgets = {
        #         'address': widgets.TextInput(attrs={'class': 'form-control', 'readonly': True}),
        #         'number': widgets.TextInput(attrs={'class': 'form-control', 'readonly': True}),
        #         'zip': widgets.TextInput(attrs={'class': 'form-control', 'readonly': True}),
        #         'description': widgets.TextInput(attrs={'class': 'form-control', 'readonly': True}),
        #         'rooms': widgets.TextInput(attrs={'class': 'form-control', 'readonly': True}),
        #         'size': widgets.TextInput(attrs={'class': 'form-control', 'readonly': True}),
        #         'price': widgets.TextInput(attrs={'class': 'form-control', 'readonly': True}),
        #         'category': widgets.TextInput(attrs={'class': 'form-control', 'readonly': True}),
        #         'seller': widgets.TextInput(attrs={'class': 'form-control', 'readonly': True}),
        #     }


class ApartmentUpdateForm(ModelForm):
    class Meta:
        model = Apartment
        exclude = ['id', 'created', 'updated']
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
            'owner_phone': widgets.NumberInput(attrs={'class': 'form-control'}),
            'sold': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
            'buyer_id': widgets.NumberInput(attrs={'class': 'form-control'})
        }


class ApartmentAddForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Apartment
        exclude = ['id', 'created', 'updated', 'sold', 'buyer_id']
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
