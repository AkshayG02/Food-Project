from django import forms
from .models import Food

class FoodForm(forms.ModelForm):
    class Meta:
        models:Food




class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
