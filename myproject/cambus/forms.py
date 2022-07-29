from django import forms

class RegisterForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea)