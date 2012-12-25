from django.shortcuts import render_to_response,get_object_or_404
from django.http import HttpResponseRedirect
from rent.models import Pr,Contract
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.forms import ModelForm
from django.core.context_processors import csrf 

#ContractForm++++++++++++++++++++++++++++++++
class ContractForm(ModelForm):
	class Meta:
		model = Contract

@login_required
def add_contract(request):
	if request.method == 'POST':
		form = ContractForm(data=request.POST)
		if form.is_valid():
			new_contract = form.save()
			return HttpResponseRedirect(new_contract.get_absolute_url())
	else:
		form = ContractForm()
	return render_to_response('rent/contract_form.html',{'form':form,'add':True},context_instance=RequestContext(request,processors=[csrf]))

@login_required
def edit_contract(request,contract_id):
	contract = get_object_or_404(Contract,pk=contract_id)
	if request.method == 'POST':
		form = ContractForm(instance=contract,data=request.POST)
		if form.is_valid():
			contract = form.save()
			return HttpResponseRedirect(contract.get_absolute_url())
	else:
		form = ContractForm(instance=contract)
	return render_to_response('rent/contract_form.html',{'form':form,'add':False},context_instance=RequestContext(request,processors=[csrf]))

#ConrtactForm End++++++++++++++++++++++++++++++++


#PrForm++++++++++++++++++++++++++++++++++++++++++
class PrForm(ModelForm):
	class Meta:
		model = Pr

@login_required
def add_pr(request,contract_id):
	if request.method == 'POST':
		form = PrForm(data=request.POST)
		if form.is_valid():
			new_pr = form.save()
			new_pr.save()
			return HttpResponseRedirect(new_pr.contract.get_absolute_url())
	else:
		contract = get_object_or_404(Contract,pk=contract_id)
		form = PrForm(initial={'contract':contract})
	return render_to_response('rent/pr_form.html',{'form':form,'add':True},context_instance=RequestContext(request,processors=[csrf]))

@login_required
def edit_pr(request,pr_id):
	pr = get_object_or_404(Pr,pk=pr_id)
	if request.method == 'POST':
		form = PrForm(instance=pr,data=request.POST)
		if form.is_valid():
			pr = form.save()
			return HttpResponseRedirect(pr.contract.get_absolute_url())
	else:
		form = PrForm(instance=pr)
	return render_to_response('rent/pr_form.html',{'form':form,'add':False},context_instance=RequestContext(request,processors=[csrf]))

@login_required
def delete_pr(request,pr_id):
	pr = get_object_or_404(Pr,pk=pr_id)
	contract = pr.contract
	if request.method == 'POST':
		if request.POST['del_pr'] == 'yes':
			pr.delete()
		elif request.POST['del_pr'] == 'no':
			pass
		return HttpResponseRedirect(contract.get_absolute_url())
	else:
		pass# return HttpResponseRedirect(contract.get_absolute_url())
	return render_to_response('rent/pr_delete_confirm.html',{'pr':pr},context_instance=RequestContext(request,processors=[csrf]))
#PrForm End++++++++++++++++++++++++++++++++++++++

@login_required
def contact_list(request):
	contract_list = Contract.objects.all()
	return render_to_response('rent/contract_list.html',{'contract_list':contract_list},context_instance=RequestContext(request))



@login_required
def contact_detail(request,id):
	contract_detail = get_object_or_404(Contract,pk=id)
	pr_list = Pr.objects.filter(contract=id)
	return render_to_response('rent/contract_detail.html',
							  {'contract':contract_detail,
							   'pr_list':pr_list},
							  context_instance=RequestContext(request)
							  )
@login_required
def pay_records_list(request):
	records_list = Pr.objects.all()
	return render_to_response('rent/pay_records_list.html',{'record_list':records_list},context_instance=RequestContext(request))

@login_required
def pay_record_detail(request,id):
	record_detail = get_object_or_404(pd==id)
	return render_to_response('rent/pay_record_detail',{'record_detail':record_detail},context_instance=RequestContext(request))

@login_required
def search_contract(request):
	query = request.GET.get('name','')
	results = []
	if query:
		results = Contract.objects.filter(client__icontains=query)
	return render_to_response('rent/search_contract.html',{'query':query,
								  'results':results},context_instance=RequestContext(request))

@login_required	
def search_pay_record(request):
	query = request.GET.get('name','')
	results = []
	if query:
		results = Pr.objects.filter(contract__client__icontains=query)
	return render_to_response('rent/search_pr.html',{'query':query,
								'results':results},context_instance=RequestContext(request))