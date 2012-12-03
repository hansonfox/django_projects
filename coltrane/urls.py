from django.conf.urls.defaults import *
from coltrane.models import Category,Entry,Link

entry_info_dict = {'queryset':Entry.objects.all(),
					'date_field':'pub_date'}

link_info_dict = {'queryset':Link.objects.all(),
					'date_field':'pub_date'}
                    
urlpatterns = patterns('django.views.generic.date_based',
    (r'^$','archive_index',entry_info_dict,'coltrane_entry_archive_index'),
    (r'^(?P<year>\d{4})/$','archive_year',entry_info_dict,'coltrane_entry_archive_year'),
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/$','archive_month',entry_info_dict,'coltrane_entry_archive_month'),
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$','archive_day',entry_info_dict,'coltrane_entry_archive_day'),
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$','object_detail',entry_info_dict,'coltrane_entry_detail'),

    (r'^link/$','archive_index',link_info_dict,'coltrane_link_archive_index'),
    (r'^link/(?P<year>\d{4})/$','archive_year',link_info_dict,'coltrane_link_archive_year'),
    (r'^link/(?P<year>\d{4})/(?P<month>\w{3})/$','archive_month',link_info_dict,'coltrane_link_archive_month'),
    (r'^link/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$','archive_day',link_info_dict,'coltrane_link_archive_day'),
    (r'^link/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)$','object_detail',link_info_dict,'coltrane_link_detail'),

)

urlpatterns += patterns('',
	(r'^categories/$','django.views.generic.list_detail.object_list',{'queryset':Category.objects.all()}),
	(r'^categories/(?P<slug>[-\w]+)/$','coltrane.views.category_detail'),
)
