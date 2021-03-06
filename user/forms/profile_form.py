from django.forms import ModelForm, widgets
from user.models import Profile
from crispy_forms.helper import FormHelper


class ProfileForm(ModelForm):
    helper = FormHelper()
    helper.form_show_labels = False

    class Meta:
        model = Profile
        exclude = ['id', 'user']
        widgets = {
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'phone': widgets.TextInput(attrs={'class': 'form-control'}),
            'image': widgets.TextInput(attrs={'class': 'form-control'})
        }

