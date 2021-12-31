from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import FarmeruploadForm,ContactUsForm
from Home.models import farmer,buyer,Farmerupload,ContactUs
from django.contrib import messages


#Here Logic of data base Registration to user input
def FarmerUpload(request):
    if request.method=='POST':
        form = FarmeruploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            # Get the current instance object to display in the template
            #img_obj = form.instance
            return render(request, 'DisplayProduce.html', {'form': form})#'img_obj': img_obj
    else:
        form = FarmeruploadForm()
    return render(request, 'ProduceUpload.html', {'form': form})

def DisplayToBuyerProduces(request):
        if request.method == 'GET':
            form=FarmeruploadForm()
            AllProduces=Farmerupload.objects.all()
            return render(request,'BuyForm.html',{'data':AllProduces})



def ContactUS(request):
    if request.method=='POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Request Submmited, Contact You Soon')
            form=ContactUsForm()

            # Get the current instance object to display in the template
            #img_obj = form.instance
            return http.HttpResponseRedirect('Contact')#'img_obj': img_obj
    else:
        form = ContactUsForm()
        messages.info(request, 'Form Fills Properly')
    return render(request,'Contact.html',{'form':form})


# Create your views here.
def HomePage(request):
    return render(request,'MainIndex.html')

def ServicesUS(request):
    return render(request,'Services.html')
    
def searchProduces(request):
    return render(request,'SearchProduces.html')

def HelpUS(request):
    return render(request,'Help.html')


def AboutUS(request):
    return render(request,'About.html')

def DisplayProduce(request):
    return render(request,'DisplayProduce.html')



