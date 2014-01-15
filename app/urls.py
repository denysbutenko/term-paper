from django.conf.urls import *
from django.contrib import admin
from django.contrib.admin import site

from django.views.generic import RedirectView

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', RedirectView.as_view(url="auth/user"), name='index'),
    url(r'^auth/user', 'auth.views.user'),
    url(r'^auth/vhost', 'auth.views.vhost'),
    url(r'^auth/resource', 'auth.views.resource'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # enable the admin:
    url(r'^admin/', include(site.urls)),
)
