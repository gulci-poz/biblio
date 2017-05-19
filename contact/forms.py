from django import forms

from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('name', 'email', 'message')


# formularz bez użycia zdefiniowanego wcześniej modelu
class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea())

    def clean_name(self):
        # cleaned_data zawiera poprawne dane,
        # tutaj możemy je dalej weryfikować
        data = self.cleaned_data['name']
        if 'S' not in data:
            raise forms.ValidationError("Musisz mieć imię zawierające 'S'.")
        return data
