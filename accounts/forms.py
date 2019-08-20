from django import forms
from .models import Cv


class NewCv(forms.ModelForm):
    class Meta:
        model = Cv
        fields = ('full_name', 'age', 'city', 'note', 'specialization')