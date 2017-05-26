from django.conf import settings
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView


def home(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))


class MainPageView(TemplateView):
    template_name = 'index.html'


# as_view() zwraca funkcję widoku
index_view = MainPageView.as_view()

favicon_view = RedirectView.as_view(
    url=settings.STATIC_URL + 'biblio/img/library-favicon.png',
    permanent=True)
