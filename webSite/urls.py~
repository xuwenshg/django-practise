from django.conf.urls.defaults import patterns, include, url
from webSite.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webSite.views.home', name='home'),
    # url(r'^webSite/', include('webSite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),

    url(r'^$',index),
    url(r'^index/$',index),
    url(r'^date/$',date),
    url(r'^time/(\d{1,2})/$',head_hour),
    url(r'^current_time/$',current_time),
    url(r'^base/$',base),
    url(r'^show_note/$',show_note),
    url(r'^add_note/$',add_note),
)
