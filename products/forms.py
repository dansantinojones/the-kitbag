from django import forms
from .models import Shirt, League, SellShirt


class ShirtForm(forms.ModelForm):
    class Meta:
        model = Shirt
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        leagues = League.objects.all()
        friendly_names = [(l.id, l.get_friendly_name()) for l in leagues]

        self.fields['league'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'



class SellShirtForm(forms.ModelForm):
    class Meta:
        model = SellShirt
        fields = ('team_name', 'home_away_third', 'league',
                  'year', 'size', 'condition', 'additional_info',
                  'image_front', 'image_back', 'full_name',
                  'email', 'phone_number',)

    def __init__(self, *args, **kwargs):
        """ Add placeholders """
        super().__init__(*args, **kwargs)
        placeholders = {
            'team_name': 'Team Name',
            'home_away_third': 'Home, Away or Third Shirt',
            'league': 'League ',
            'year': 'Year',
            'size': 'Shirt Size',
            'condition': 'Condition of the Shirt',
            'additional_info': 'Additional Information',
            'full_name': 'Your Name',
            'email': 'Your Email',
            'phone_number': 'Your Phone Number',
        }