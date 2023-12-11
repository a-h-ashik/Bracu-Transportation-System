from django import forms
from homepage.models import Lost

class Lostitem(forms.ModelForm):
    class Meta:
        model=Lost
        fields=['name','email','lostitem','description']