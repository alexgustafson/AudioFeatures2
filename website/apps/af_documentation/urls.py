from django.conf.urls import patterns, url
from af_documentation import views

urlpatterns = patterns('af_documentation.views',
    url(r'^sections/$', views.SectionList.as_view(), name="section-list"),
    url(r'^sections/(?P<pk>[0-9]+)/$', views.SectionDetail.as_view(), name="section-detail"),
    url(r'^contentnodes/$', views.ContentNodeList.as_view(), name="contentnode-list"),
    url(r'^contentnodes/(?P<pk>[0-9]+)/$', views.ContentNodeDetail.as_view(), name="contentnode-detail"),
    url(r'^contenttypes/$', views.ContentTypeList.as_view(), name="plugin-list"),
    url(r'^contenttypes/(?P<pk>[0-9]+)/$', views.ContentTypeDetail.as_view(), name="plugin-detail"),
)