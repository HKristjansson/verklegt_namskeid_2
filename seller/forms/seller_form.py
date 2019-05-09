from django.forms import ModelForm, widgets
from django import forms
from seller.models import Seller

class SellerUpdateForm(ModelForm):
    class Meta:
        model = Seller
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'image': widgets.NumberInput(attrs={'class': 'form-control'}),
            'year_of_start': widgets.TextInput(attrs={'class': 'form-control'})
            #'available': widgets.CheckboxInput(attrs={'class': 'checkbox'})
        }


class SellerAddForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Seller
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'image': widgets.NumberInput(attrs={'class': 'form-control'}),
            'year_of_start': widgets.TextInput(attrs={'class': 'form-control'}),
            'available': widgets.CheckboxInput(attrs={'class': 'checkbox'})
        }
