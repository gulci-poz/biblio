from django.views.generic.edit import CreateView

from .forms import BookRentForm
from .models import Rental


class BookRentView(CreateView):
    model = Rental

    # jeśli używamy form_class, to nie możemy definiować fields
    # to pole jest już w definicji formularza
    form_class = BookRentForm
    # fields = ['who', 'what']

    # domyślnie uruchamia się get_absolute_url
    success_url = '/rental/rent'
