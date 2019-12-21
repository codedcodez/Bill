from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True, max_length=100)
    message = forms.CharField(required=True, widget=forms.Textarea)
