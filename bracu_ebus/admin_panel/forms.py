from django import forms
from .models import Staff, Admin

class AdminLoginForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ["name", "password"]
        widgets = {'password':forms.PasswordInput}

class CreateStaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ["name", "email"]