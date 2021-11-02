from django import forms
from django.db.models import query
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth  import authenticate,  login
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect,ensure_csrf_cookie
from .forms import form
from task.forms import form
from .models import Users
#@csrf_protect

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email,password=password)
      
        return redirect("display")
        # if user is not None:
        #     print('here')
        #     auth.login(request, user)
        #     return redirect("display")
        # else:
        #     messages.info(request,'invalid credentials')
        #     return redirect('login')

    else:
        return render(request,'index.html')    

def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        address = request.POST['address']
        

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username Taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('signup')
            else:   
                user = User.objects.create_user(username=username, password=password1, email=email)
                add_user =  Users.objects.create(address=address,user=user)
                add_user.save()
               # user.save()

                print('user created')
                return redirect('display')

        else:
            messages.info(request,'password not matching..')    
            return redirect('signup')
        return redirect('/')
        
    else:
        return render(request,'signup.html')

def display(request):
    users = Users.objects.all()
    
    return render(request,'display.html',{'users':users})

def remove(request,username):
    item = User.objects.get(username=username)
    item.delete()
    users = Users.objects.all()
    return render(request,'display.html',{'users':users})

def update(request,username):
    user = User.objects.get(username=username)
    forms = form(request.POST or None,instance=user)
    if forms.is_valid():
        forms.save()
        return render(request,'display.html',{'Users':user})
    return render(request,'display.html',{'Users':user})

# def logout(request):
    
#     auth.logout(request)
#     return render(request,'index.html')