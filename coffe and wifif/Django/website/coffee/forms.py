from django import forms
from .models import CafeData

class CafeForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = CafeData