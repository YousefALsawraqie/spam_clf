# forms.py file content will go herefrom django import forms

from django import forms

class MessageForm(forms.Form):
    messages = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 50}), label='الرسائل')