from django.views.generic import TemplateView
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^poll/(?P<pk>[0-9]+)$', 'apps.polls.views.get_poll', name='get_poll'),
    url(r'^poll/save$', 'apps.polls.views.save_poll_results', name='save_poll_results'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^.*$', TemplateView.as_view(template_name="index.html")),
)
