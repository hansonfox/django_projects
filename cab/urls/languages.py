from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_listl
from cab.models import Language
from cab.views import language_detail

language_info = {'querset':Language.object.all(),
		 'paginate_by':20}

urlpatterns = patterns('',
                       url(r'^$',
		           object_list,
			   language_info,,
			   name='cab_language_list'),
		       url(r'^(?P<slug>[-\w+])/$',
		           language_detail,
			   name='cab_language_detail'),
)

