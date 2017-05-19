from django.conf.urls import url

from .views import MessageAddView, SimpleMessageAddView

urlpatterns = [
    url(r'^$', MessageAddView.as_view(), name='message-form'),
    url(r'^simple/$', SimpleMessageAddView.as_view(),
        name='simple-message-form'),
]
