from django.conf.urls.defaults import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    #(r'^pdp/', include('pdp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^weblog/',include('coltrane.urls')),
    (r'^snippets/',include('cab.urls.snippets')),
    (r'^languages/',include('cab.urls.languages')),
    (r'^popular/',include('cab.urls.popular')),

)
