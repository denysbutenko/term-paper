from django.conf.urls import *
from django.contrib import admin
from django.contrib.admin import site

from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name="base.html"), name='index'),

    # enable the admin:
    url(r'^admin/', include(site.urls)),
)
