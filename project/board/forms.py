from django import forms
from .models import Ad, Comment

class AdForm(forms.ModelForm):
    """Форма для создания и редактирования объявления."""
    class Meta:
        model = Ad
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Что вы продаете/ищете?'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }

class CommentForm(forms.ModelForm):
    """Форма для добавления комментария к объявлению."""
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Оставьте ваш комментарий...'}),
        }