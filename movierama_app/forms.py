# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm, Textarea, TextInput, PasswordInput
from django.contrib.auth.models import User
from movierama_app.models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = TextInput(attrs={
            'class':'form-control'
        })
        self.fields['password'].widget = PasswordInput(attrs={
            'class':'form-control'
        })

class NewMovie(ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'description')
    def __init__(self, *args, **kwargs):
        super(NewMovie, self).__init__(*args, **kwargs)
        self.fields['description'].widget = Textarea(attrs={
            'cols':50,
            'rows': 10,
            'class':'form-control'
        })
        self.fields['title'].widget = TextInput(attrs={
            'class':'form-control'
        })