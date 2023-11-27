from django import forms
from .models import Staff, Admin

from ticket_booking.models import Buses

class AdminLoginForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ["name", "password"]
        widgets = {'password':forms.PasswordInput}

class CreateStaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ["name", "email"]

class RouteCreationForm(forms.ModelForm):
    class Meta:
        model = Buses
        fields = ['bus_number', 'd1', 'd2', 'd3', 'd4', 'd5', 'active']
