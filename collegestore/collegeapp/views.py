
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    if request.method== 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('form')
        else:
            return redirect('login')

    return render(request,"login.html")


def register(request):
    if request.method== 'POST':
        username=request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password)

            user.save();
            return redirect('login')

        else:
            messages.info(request,"password not matching!!!")
            return redirect('register')
        return redirect('/')
    return render(request, "register.html")


def form(request):
    return render(request,"form.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def success(request):
    return render(request,"success.html")