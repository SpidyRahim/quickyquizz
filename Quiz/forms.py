from dataclasses import fields
from pyexpat import model
from django import forms
from django.contrib.auth.models import User
from . import models


class CreateQuizForm(forms.ModelForm):
    class Meta:
        model = models.Quiz
        fields = ['quiz_name', 'instructions']
        widgets = {
            'instructions': forms.Textarea(attrs={'rows': 4, 'cols': 50})
        }


class AddQuestion(forms.ModelForm):
    quiz_id = forms.ModelChoiceField(
        queryset=models.Quiz.objects.all(), empty_label="--", to_field_name="id")

    class Meta:
        model = models.Question
        fields = ['question', 'option1', 'option2', 'option3', 'answer']
        widgets = {
            'question': forms.Textarea(attrs={'rows': 3, 'cols': 50})
        }
