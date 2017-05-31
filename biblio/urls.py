"""biblio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from . import views
from .api_config import router as api_config_router

urlpatterns = [
                  # url(r'^$', views.home, name='home'),
                  url(r'^$', views.index_view, name='main-page'),
                  url(r'^admin/', admin.site.urls),
                  url(r'^shelf/', include('shelf.urls', namespace='shelf')),
                  url(r'^contact/',
                      include('contact.urls', namespace='contact')),
                  url(r'^accounts/', include('allauth.urls')),
                  url(r'^rental/', include('rental.urls', namespace='rental')),
                  url(r'^favicon\.ico$', views.favicon_view),
                  url(r'^api/', include(api_config_router.urls)),
                  # np. api/auth/login
                  url(r'^api/auth/', include('rest_framework.urls',
                                             namespace='rest_framework')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
