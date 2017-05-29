from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy

from .models import Rental


class BookRentView(CreateView):
    model = Rental
    fields = ['who', 'what']
    success_url = '/rental/rent'
