from django.contrib.auth.models import User
from django import forms

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            'username': forms.TextInput({'placeholder': 'Username'}),
            'email': forms.EmailInput({'placeholder': 'Email'}),
            'password': forms.PasswordInput({'placeholder': 'Password'}),
        }
        
        
class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password')
        widgets = {
            'email': forms.EmailInput({'placeholder': 'Email'}),
            'password': forms.PasswordInput({'placeholder': 'Password'}),
        }