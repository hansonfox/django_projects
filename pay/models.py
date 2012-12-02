#coding=utf-8
from django.db import models

class Person(models.Model):
	STATUS_LIVE = '1'
	STATUS_STOP = '0' 
	STATUS = (
		(STATUS_LIVE,'LIVE'),
		(STATUS_STOP,'STOP'),
		)

	name = models.CharField(max_length=10)
	idnum = models.CharField(max_length=20)
	reunit = models.CharField(max_length=25) #
	ui_num = models.CharField(max_length=15) #
	phone = models.CharField(max_length=11,blank=True)
	status = models.CharField(max_length=1,choices=STATUS,default=STATUS_LIVE)#

	class Meta:
		ordering = ['-id']

	def __unicode__(self):
		return '%s %s %s' % (self.name,self.idnum,self.reunit)

	@models.permalink
	def get_absolute_url(self):
		return  ('records_detail',(),{'id':self.id})

class Record(models.Model):

	FLAG_CHOICES = (
		(u'正常',u'一次申领'),
		(u'二次',u'二次申领'),
		(u'终止',u'终止'),
		)
	person = models.ForeignKey(Person)
	begin_date = models.DateField() 
	end_date = models.DateField() # end_date always >=begin_date
	flag = models.CharField(max_length=10,choices=FLAG_CHOICES,default=FLAG_CHOICES[0][0])
	pay_std = models.DecimalField(max_digits=7,decimal_places=2)
	note = models.TextField(max_length=50,blank=True)
	rec_date = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-rec_date']

	def __unicode__(self):
		return self.person.name

	def get_absolute_url():
		return 'payment/record/?=%s' % self.id

