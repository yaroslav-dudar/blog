from django.views.generic import TemplateView
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^api/', include('apps.polls.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^.*$', TemplateView.as_view(template_name="index.html")),
)
