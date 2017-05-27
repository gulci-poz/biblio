from django import forms

from .models import Rental


class BookRentForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['who', 'what']
