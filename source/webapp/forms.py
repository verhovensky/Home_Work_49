from django import forms
from webapp.models import Todolist


class TodolistForm(forms.ModelForm):

    class Meta:
        model = Todolist
        fields = '__all__'
        error_messages = {
            'name': {
                'required': 'The field is required to be filled'
            }
        }