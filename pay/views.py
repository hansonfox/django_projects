#coding=utf-8
from django.shortcuts import render_to_response
from pay.models import Record,Person
import datetime

def records_index(self):
	'''show all records list'''
	return render_to_response('records_index.html',
								{'record_list':Record.objects.all().order_by('-begin_date','-end_date') }
							 )

def records_detail(self,id):
	'''show records belong to one person'''
	return render_to_response('records_detail.html',
								{ 'person':Person.objects.get(id=id),
								  'record_list':Record.objects.filter(person=id).order_by('rec_date') }
							)

def person_index(self):
	return render_to_response('person_index.html',
								{'person_list':Person.objects.all().order_by('-id') } 
							 )

def current(self):
	return render_to_response('current_list.html',
								{'new_list':Record.objects.filter(begin_date__year=datetime.date.today().year,begin_date__month=datetime.date.today().month) , 
								 'stopped_list':Record.objects.filter(end_date__year=datetime.date.today().year,end_date__month=datetime.date.today().month+1),
								 'first_pay':Record.objects.filter(flag=u'正常').filter(end_date__gte=datetime.date.today()), 
								 'second_pay':Record.objects.filter(flag=u'二次').filter(end_date__gte=datetime.date.today()) 
								 })


# def past_post(self,year,month):
# 	return render_to_response('past_post.html',
# 								{'new_list':Record.objects.filter(begin_date__year=year,begin_date__month=month) , 
# 								 'stopped_list':Record.objects.filter(end_date__year=year,end_date__month=month+1),
# 								 'first_pay':Record.objects.filter(flag=u'正常').filter(end_date__gte=datetime.date.today()), 
# 								 'second_pay':Record.objects.filter(flag=u'二次').filter(end_date__gte=datetime.date.today()) 
# 								 })

