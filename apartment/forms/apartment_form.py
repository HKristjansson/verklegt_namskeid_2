from django.forms import ModelForm, widgets, forms
from django import forms
from apartment.models import Apartment

class ApartmentBuyForm(forms.ModelForm):
    class Meta:
        model = Apartment
        exclude = ['id', 'created', 'updated']
        readonly_fields = ['address', 'number', 'zip', 'description', 'rooms', 'size', 'price', 'category',
                           'seller', 'owner_name', 'owner_ssn', 'owner_phone']

        widgets = {
            'address': widgets.TextInput(attrs={'readonly': True}),
            'number': widgets.TextInput(attrs={'readonly': True}),
            'zip': widgets.TextInput(attrs={'readonly': True}),
            'description': widgets.TextInput(attrs={'readonly': True}),
            'rooms': widgets.TextInput(attrs={'readonly': True}),
            'size': widgets.TextInput(attrs={'readonly': True}),
            'price': widgets.TextInput(attrs={'readonly': True}),
            'category': widgets.TextInput(attrs={'readonly': True}),
            'seller': widgets.TextInput(attrs={'readonly': True}),
            'owner_name': widgets.TextInput(attrs={'readonly': True}),
            'owner_ssn': widgets.TextInput(attrs={'readonly': True}),
            'owner_phone': widgets.TextInput(attrs={'readonly': True})




            # 'number': widgets.NumberInput(attrs={'class': 'form-control'}),
            # 'zip': widgets.NumberInput(attrs={'class': 'form-control'}),
            # 'description': widgets.TextInput(attrs={'class': 'form-control'}),
            # 'rooms': widgets.NumberInput(attrs={'class': 'form-control'}),
            # 'size': widgets.NumberInput(attrs={'class': 'form-control'}),
            # 'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            # 'category': widgets.Select(attrs={'class': 'form-control'}),
            # 'seller': widgets.Select(attrs={'class': 'form-control'}),
            # 'owner_name': widgets.TextInput(attrs={'class': 'form-control'}),
            # 'owner_ssn': widgets.NumberInput(attrs={'class': 'form-control'}),
            # 'owner_phone': widgets.NumberInput(attrs={'class': 'form-control'}),
            # 'sold': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
            # 'buyer_id': widgets.NumberInput(attrs={'class': 'form-control'})
        }

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
