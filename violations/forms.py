from django import forms
from violations.models import Violation


class ViolationForm(forms.ModelForm):
    class Meta:
        model=Violation
        fields=["description","image"]


    