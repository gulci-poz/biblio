from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView


def home(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))


class MainPageView(TemplateView):
    template_name = 'index.html'


# as_view() zwraca funkcję widoku
index_view = MainPageView.as_view()
