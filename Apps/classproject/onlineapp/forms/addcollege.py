from django import forms
from onlineapp.models import College


class AddCollege(forms.ModelForm):
    class Meta:
        model = College
        exclude = ['id']
        fields = ['name', 'location', 'acronym', 'contact']