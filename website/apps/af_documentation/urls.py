from django.conf.urls import patterns, url

urlpatterns = patterns('af_documentation.views',
    url(r'^sections/$', 'section_list'),
    url(r'^sections/(?P<pk>[0-9]+)/$', 'section_detail'),
    url(r'^contentnodes/$', 'contentnode_list'),
    url(r'^contentnodes/(?P<pk>[0-9]+)/$', 'contentnode_detail'),
)