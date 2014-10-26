from django import forms
from eventRegistrations import models

class RegistrationForm(forms.Form):
    members = forms.CharField(widget=forms.Textarea,required=True,help_text="Enter name followed by roll no. One member per line.")
    contact_number = forms.DecimalField(max_digits=10,decimal_places=0,required=True)
    alternate_contact_number = forms.DecimalField(max_digits=10,decimal_places=0,required=False)
