from django import forms
from .models import User, AccountRequestTable

class RegistrationForm(forms.ModelForm):
    password_again =  forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        widgets = {'password':forms.PasswordInput}

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {'password':forms.PasswordInput}
        
class AccountRequestForm(forms.ModelForm):
    class Meta:
        model = AccountRequestTable
        fields = ['name', 'email', 'description']
        widgets = {'description':forms.Textarea}
