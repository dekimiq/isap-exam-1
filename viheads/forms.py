from django import forms
from .models import Idea

class IdeaForm(forms.ModelForm):
  class Meta:
    model = Idea
    fields = ['title', 'description', 'difficulty']
    widgets = {
      'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Введите название'}),
      'description': forms.Textarea(attrs={'class': 'form-input', 'placeholder': 'Введите описание', 'rows': 3}),
      'difficulty': forms.Select(attrs={'class': 'form-select'})
    }