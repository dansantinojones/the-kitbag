from django import forms
from .models import Newsletter


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ('email',)

    def clean_email(self):
        email = self.cleaned_data.get('email')

        return email

