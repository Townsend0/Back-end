from django import forms
from .models import BookData

class BookForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = BookData
