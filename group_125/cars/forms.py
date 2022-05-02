from django import forms
from .models import *

class AddForm(forms.Form):
    topic = forms.CharField(max_length=50,label='тема')
    comment = forms.CharField(
        label='комментарий',
        widget = forms.Textarea(
            attrs={'class':'form-control','rows':5,'cols':20,'placeholder':'Ваш комментарий'}
        )
    )
    is_published = forms.BooleanField(label='опубликовано',initial=True)

class CarForm(forms.ModelForm):
    class Meta():
        model = Car
        fields = ['title','costs','content','company']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 5}),
        }
