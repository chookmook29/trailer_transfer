from django import forms
from .models import Door


class DoorForm(forms.ModelForm):
    class Meta:
        model = Door
        fields = ['trailer_number', 'status']