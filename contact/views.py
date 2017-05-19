from django.views.generic import FormView

from .forms import ContactForm, MessageForm


class MessageAddView(FormView):
    form_class = MessageForm
    template_name = 'contact/message_form.html'
    success_url = '/contact'

    def form_valid(self, form):
        # mamy dostępny formularz pod zmienną form (podobnie jak z modelem)
        # możemy używać metod tego obiektu
        # dzięki save() dodamy dane do modelu i zapiszemy w bazie danych
        form.save()
        return super(MessageAddView, self).form_valid(form)


# wysyłanie formularza bez zapisu do bazy danych
class SimpleMessageAddView(FormView):
    form_class = ContactForm
    template_name = 'contact/simple_message_form.html'
    success_url = '/contact/simple'
