from django import forms
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title','content','categories','image']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']


class CategoryForm(forms.Form):
    categories = forms.ModelMultipleChoiceField(
        queryset=Categories.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )