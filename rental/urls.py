from django.conf.urls import url

from .views import BookRentView

urlpatterns = [
    url('^rent/$', BookRentView.as_view(), name='book-rent'),
]
