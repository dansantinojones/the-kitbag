from django import forms
from .models import Review


class PostReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('full_name', 'email', 'rating', 'body',)