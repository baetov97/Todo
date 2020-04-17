from django import forms
from .models import *


class ToDoForm(forms.ModelForm):
    text = forms.CharField(max_length=40, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter todo e.g. Delete junk files', 'aria-label': 'ToDo',
               'aria-describedby': 'add-btn'}))


class NewTodoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ['text']
        widgets = {
            'text': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter todo e.g. Delete junk files',
                       'aria-label': 'ToDo',
                       'aria-describedby': 'add-btn'})
        }
