from django.shortcuts import render, redirect, HttpResponse
from .forms import SignupForm
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from django.contrib import messages
# Create your views here.

def Signup(request):
	if request.method == 'POST' and 'action' in request.POST:
		form = SignupForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			email = form.cleaned_data.get('email')
			password = form.cleaned_data.get('password')
			User.objects.create_user(username=username, email=email, password=password)
			messages.info(request,"Your account has been successfully Registered, Now you LogIn ")
			return redirect('login')
	else:
		form = SignupForm()
		if request.user.is_authenticated:
			return redirect('addshow')
		else:
			if request.method == 'POST' and 'Signin' in request.POST:
				username = request.POST['username']
				password = request.POST['password']
				user = auth.authenticate(username=username, password=password)
				if user is not None:
					auth.login(request, user)
					return redirect('addshow')
				else:
					messages.error(request,"*Invalid User, Please Try Again & SignUp")
	context = {'formsign': form,}
	return render(request, 'sign.html', context)


def logoutUser(request):
	auth.logout(request)
	return redirect('/')