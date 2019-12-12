from django.forms import ModelForm, TextInput
from . import models


class CityForm(ModelForm):
    class Meta:
        model = models.City
        fields = ['city']
        widgets = {'city': TextInput(attrs={'class':'input', 'placeholder': 'City name'})}
