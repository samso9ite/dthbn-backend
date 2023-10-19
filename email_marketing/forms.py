from  django import forms

class emails(forms.Form):
    all_emails = forms.CharField(max_length=250)

