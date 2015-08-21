from django import forms
from archive.models import urlSites

class UrlForm(forms.ModelForm):
    class Meta:
        model = urlSites
        fields = ('originalUrl',)