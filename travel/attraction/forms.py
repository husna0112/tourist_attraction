from django import forms
from attraction.models import Plan

class CreatePlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['name', 'detail']