from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^poll/(?P<pk>[0-9]+)$', views.get_poll, name='get_poll'),
    url(r'^poll_result/save$', views.save_poll_results, name='save_poll_results'),
)