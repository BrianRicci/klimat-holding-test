from django import forms
from .models import CoffeeHouse


class CoffeeHouseForm(forms.ModelForm):
    class Meta:
        model = CoffeeHouse
        fields = ['name', 'description', 'work_time']
