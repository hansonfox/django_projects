#coding=utf-8
from django.db import models
import datetime
# Create your models here.

class Contract(models.Model):

	LIVE_STATUS = 1
	END_STATUS = 0
	FLAG_CHOICES = (
		(LIVE_STATUS,'正常'),
		(END_STATUS,'到期'),
		)

	client = models.CharField(max_length=20,verbose_name='客户')
	contract_num = models.CharField(max_length=20,verbose_name='合同编号')
	begin_date = models.DateField(verbose_name='租约开始日期')
	end_date = models.DateField(verbose_name='租约结束日期')
	month_pay = models.DecimalField(max_digits=7,decimal_places=2,verbose_name='月租金')
	flag = models.IntegerField(choices=FLAG_CHOICES,default=LIVE_STATUS,verbose_name='合同状态')

	def __unicode__(self):
		return "%s:%s:%s" % (self.contract_num,self.client,self.flag)

	@models.permalink
	def get_absolute_url(self):
		return ('contract_detail',(),{'id':self.id})


class Pr(models.Model):
	contract = models.ForeignKey(Contract,verbose_name='合同信息')
	pay_date = models.DateField(default=datetime.datetime.now,verbose_name='缴费日期')
	pay_value = models.DecimalField(max_digits=7,decimal_places=2,verbose_name='缴费金额')

	class Meta:
		ordering = ['-pay_date']

	def __unicode__(self):
		return "%s:%s:%s:%s" % (self.contract.contract_num,self.contract.client,self.pay_date,self.pay_value)

	@models.permalink
	def get_absolute_url(self):
		return ('pay_record_detail',(),{'id':self.id})
