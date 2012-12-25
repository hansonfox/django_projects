from django.conf.urls.defaults import *
# from rent.views import *
# from django.contrib.auth.views import login,logout
from django.conf import settings

urlpatterns = patterns('rent.views',

    (r'^$','contact_list'),
    (r'^contract/$','contact_list'),
	url(r'^contract/id=(?P<id>\d)/$','contact_detail',name='contract_detail'),
    (r'^pay_records/$','pay_records_list'),
    (r'^pay_record/id=(?P<id>\d+)/$','pay_record_detail','pay_record_detail'),

    (r'^contract/search_con/$','search_contract'),
    (r'^contract/search_con/?name=(?P<name>[-\w]+)/$','search_contract'),

    (r'^pay_records/search_pr/$','search_pay_record'),
    (r'^pay_records/search_pr/?name=(?P<name>[-\w]+)/$','search_pay_record'),
    url(r'^add_contract/$','add_contract',name='rent_contract_add'),
    url(r'^edit_contract/(?P<contract_id>\d+)/$','edit_contract',name='rent_contract_edit'),
    url(r'^add_pr/(?P<contract_id>\d+)/$','add_pr',name='rent_pr_add'),
    url(r'^edit_pr/(?P<pr_id>\d+)/$','edit_pr',name='rent_pr_edit'),
    url(r'^delete_pr/(?P<pr_id>\d+)/$','delete_pr',name='rent_pr_delete'),
)

urlpatterns += patterns('',

	url(r'^login/$','django.contrib.auth.views.login'),
	url(r'^logout/$','django.contrib.auth.views.logout',{'template_name':'registration/logout.html'}),
)

