from django import forms

class PeopleForm(forms.Form):
    person = forms.CharField(max_length=8)