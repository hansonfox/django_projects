from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from cab.forms import SignupForm
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def signup(request):
	if request.method == 'POST':
		form = SignupForm(data=request.POST)
		if form.is_valid():
			new_user = form.save()
			return HttpResponseRedirect("/admin")
	else:
		form = SignupForm()
	return render_to_response('cab/signup.html',{'form':form})