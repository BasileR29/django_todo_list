# -*- coding: utf-8 -*-

from django import forms

from . import models
from django.contrib.auth import get_user_model

class NoteForm(forms.ModelForm):
    class Meta:
        model = models.Note
        fields = ['titre', 'contenu', 'is_public']