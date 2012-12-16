from django.conf.urls.defaults import *
from cab.views.signup import signup

urlpatterns = patterns('',
			(r'^$',signup),
			)