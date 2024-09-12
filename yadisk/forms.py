from django import forms


class PublicUrlForms(forms.Form):
    public_key = forms.CharField(max_length=100)
