from django import forms
from .models import Post, Responses, News
import requests


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'text',
            'category',
            'photo',
            'photo2',
            'video',
            'video2',
        ]


class ResponsesForm(forms.ModelForm):
    class Meta:
        model = Responses
        fields = [
            'text',
        ]


class ResponsesForm2(forms.ModelForm):
    class Meta:
        model = Responses
        fields = [
            'status',
        ]


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = [
            'title',
            'text',
        ]

