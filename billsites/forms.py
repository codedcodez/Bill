from django import forms
from .models import MobileWebSoftware

class ContactForm(forms.Form):
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True, max_length=100)
    message = forms.CharField(required=True, widget=forms.Textarea)


class MobilewebForm(forms.ModelForm):

    class Meta():
        model = MobileWebSoftware

        fields = ['username', 'wallet', 'country', 'key']
