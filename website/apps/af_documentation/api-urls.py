from django.conf.urls import patterns, url, include
from af_documentation.api import SectionList, SectionDetail, ContentNodeList, ContentNodeDetail, ContentTypeDetail, ContentTypeList


sections_urls = patterns('',
    url(r'^/(?P<uuid>[0-9]+)$', SectionDetail.as_view(), name="section-detail"),
    url(r'^/form', 'af_documentation.views.section_form', name='section-form',),
    url(r'^', SectionList.as_view(), name="section-list"),
)

contentnodes_urls = patterns('',
    url(r'^/(?P<uuid>[0-9]+)$', ContentNodeDetail.as_view(), name="contentnode-detail"),
    url(r'^/render/(?P<uuid>\d*)$', 'af_documentation.views.rendercontent', name='contentnode-render',),
    url(r'^$', ContentNodeList.as_view(), name="contentnode-list"),
)

contenttypes_urls = patterns('',
    url(r'^/(?P<uuid>[0-9]+)$', ContentTypeDetail.as_view(), name="plugin-detail"),
    url(r'^$', ContentTypeList.as_view(), name="plugin-list"),
)

urlpatterns = patterns('',
    url(r'^sections', include(sections_urls)),
    url(r'^contentnodes', include(contentnodes_urls)),
    url(r'^contenttypes', include(contenttypes_urls)),
)