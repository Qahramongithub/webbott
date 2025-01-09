from django import forms
from .models import  Operator


class OperatorModelForm(forms.ModelForm):
    class Meta:
        model = Operator
        fields = '__all__'
