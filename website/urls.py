from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^af-api/', include('af_documentation.api-urls')),
    url(r'^jsi18n/(?P<packages>\S+?)/$', 'django.views.i18n.javascript_catalog'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)

urlpatterns += i18n_patterns('',

    url(r'^$', 'af_documentation.views.home', name='home'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

)
