from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from accounts.models import extendedfarmer

@unauthenticated_user
def login(request):
    if request.user.is_authenticated:
        return redirect("HomePage")
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                if  User.objects.filter(username=username, groups__name='Buyer').exists():
                    return redirect("buyerProfile")
                else:
                    return redirect('farmerProfile')
            else:
                messages.info(request, 'invalid credentials')
                return redirect("login")
        else:
            return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

@unauthenticated_user
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        contact=request.POST['contact']
        Address=request.POST['Address']
        state=request.POST['State']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print('Username Alread Taken')
                messages.info(request, 'Username already taken, try with different Username')
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                print('Email already in Used')
                messages.info(request, 'Email already registered, try with different Email')
                return redirect("register")
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name= last_name)
                user.save()
                otherData=extendedfarmer(Phonenumber=contact,Address=Address,state=state,user=user)
                otherData.save()
                group = Group.objects.get(name='Farmer')
                user.groups.add(group)
                messages.info(request, 'Account Created SuccessFully')
                print('Acount Created SuccessFully')
                return redirect('login')
        else:
            messages.info(request, 'Password Not Matching')
            print('Password not matching')
        print('Not a post input')
        return redirect('register')
    else:
        return render(request, 'register.html')


@unauthenticated_user
def registerbuyer(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print('Username taken')
                messages.info(request, 'Username already taken, try with different Username')
                return redirect("registerbuyer")
            elif User.objects.filter(email=email).exists():
                print('Email Taken')
                messages.info(request, 'Email already registered and in use, try with different Email')
                return redirect("registerbuyer")
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name= last_name)
                user.save()
                group = Group.objects.get(name='Buyer')
                user.groups.add(group)
                messages.info(request, 'user Created')
                print('user Created')
                return redirect('login')
        else:
            messages.info(request, 'Password not matching')
            print('Password not matching')
        print('Not a post input')
        return redirect('registerbuyer')
    else:
        return render(request, 'registerBuyer.html')


@login_required(login_url='login')
def ShowBuyerorFarmerprofile(request):
    if django_user.groups.filter(name = 'Farmer').exists() :
    #if user.groups.filter(name = 'Farmer').exists() :
        return redirect('farmerProfile')
    else:
        return redirect('buyerProfile')


@login_required(login_url='login')
def farmerProfile(request):
   # data=extendedfarmer.objects.filter(user=User.objects.filter(name=self.request.user))
    users= request.user
    data=extendedfarmer.objects.filter(user= users)
    data=list(data)
    print(data)
    return render(request,'FarmerPorfile.html',{'form':data})

@login_required(login_url='login')
def buyerProfile(request):
    return render(request,'BuyerProfile.html')

def SellForm(request):
    return render(request,'SellForm.html')

def BuyForm(request):
    return render(request,'BuyForm.html')

