from django import forms
from .models import UrlShortener


class UrlShortenerForm(forms.ModelForm):
    long_url = forms.URLField(widget=forms.URLInput(
        attrs={"class": "form-control form-control-lg", "placeholder": "Insert your URL to shorten"}))

    class Meta:
        model = UrlShortener
        fields = ('long_url',)
