from django import forms
from .models import *
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class register(forms.ModelForm):
    content = forms.CharField(widget=SummernoteWidget(attrs={'summernote': {'width': '95%', 'height': '400px'}}))
    class Meta:
        model = user
        fields = ['name','email','city','phone','content']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'phone':forms.NumberInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.TextInput(attrs={'class':'form-control'}),
        }