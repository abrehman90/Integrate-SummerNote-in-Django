from django.shortcuts import render,HttpResponseRedirect,redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
# Create your views here.


@login_required()
def add_and_show(request):
    dat = user.objects.all()
    if request.method == 'POST':
        de = register(request.POST)
        if de.is_valid():
            de.save()
            de = register()
    else:
        de = register()
        dat = user.objects.all()
    return render(request,'addandshow.html',{'show':de,'data':dat})


@login_required()
def update_data(request,id):
    if request.method == 'POST':
        up = user.objects.get(pk=id)
        de = register(request.POST,instance=up)
        if de.is_valid():
            de.save()
            return redirect('/')
    else:
        up = user.objects.get(pk=id)
        de = register(instance=up)
    return render(request,'update.html',{'form':de})

@login_required()
def deletedata(request,id):
    if request.method == 'POST':
        delt = user.objects.get(pk=id)
        delt.delete()
        return HttpResponseRedirect('/')