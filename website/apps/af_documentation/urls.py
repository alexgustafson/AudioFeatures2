from django.conf.urls import patterns, url

urlpatterns = patterns('af_documentation.views',
    url(r'^snippets/$', 'section_list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', 'section_detail'),
)