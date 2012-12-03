from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_list,object_detail
from cab.models import Snippet

snippet_info = {'querset':Snippet.object.all()}

urlpatterns = patterns('',
                       url(r'^$',
		           object_list,
			   dict(snippet_info,paginate_by=20),
			   name='cab_snippet_list'),
		       url(r'^(?P<bject_id>\d+)/$',
		           object_detail,
			   snippet_info,
			   name='cab_snippet_detail'),
)

