from django import forms
from .models import TreeDataEntry

class TreePlantingForm(forms.ModelForm):
    class Meta:
        model = TreeDataEntry
        fields = '__all__'  # Include all fields in the form
