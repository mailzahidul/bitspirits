from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
                    'name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name*'}),
                    'mail' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Mail*'}),
                    'message' : forms.Textarea(attrs={'class':'form-control', 'placeholder':'Message*'})
                }