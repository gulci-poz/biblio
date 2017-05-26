from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.utils.decorators import method_decorator

from .models import Author, Book


@method_decorator(login_required, name='dispatch')
class AuthorListView(ListView):
    model = Author

    # przed django 1.9 nie mogliśmy dekorować klasy za pomocą method_decorator
    # trzeba było nadpisać metodę dispatch()
    # @method_decorator(login_required)
    # def dispatch(self, request, *args, **kwargs):
    #     super(AuthorListView, self).dispatch(request, *args, **kwargs)


class AuthorDetailView(DetailView):
    model = Author


class BookListView(ListView):
    model = Book


class BookDetailView(DetailView):
    model = Book
