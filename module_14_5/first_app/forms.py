from django import forms
from django.core import validators
from django.forms.widgets import NumberInput
import datetime

FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]

class contactForm(forms.Form):
   name = forms.CharField()
   comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
   email = forms.EmailField()
   agree = forms.BooleanField()
   birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
   value = forms.DecimalField()
   message = forms.CharField(
	max_length = 10,
)
   day = forms.DateField(initial=datetime.date.today)
   FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]
#    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
   favorite_color = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
   first_name = forms.CharField(max_length = 200) 
   last_name = forms.CharField(max_length = 200) 
   roll_number = forms.IntegerField( 
                     help_text = "Enter 6 digit roll number"
                     ) 
   password = forms.CharField(widget = forms.PasswordInput())