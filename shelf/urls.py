from django.conf.urls import url

from .views import AuthorDetailView, AuthorListView

# alternatywnie do namespace w include() w nadrzędnym pliku urls.py
# app_name = 'shelf'

urlpatterns = [
    url(r'^authors/$',
        AuthorListView.as_view(),
        name='author-list'),

    url(r'^authors/(?P<pk>\d+)/$',
        AuthorDetailView.as_view(),
        name='author-detail'),
]
