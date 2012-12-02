from django.conf.urls.defaults import *


urlpatterns=patterns('pay.views',
			url(r'^$','current'),
			url(r'^records$','records_index'),
			url(r'^person/$','person_index'),
			url(r'^person/(?P<id>\d)/$','records_detail',name='records_detail'),
			#url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$','past_post',name='past_post') #for history records.
			)