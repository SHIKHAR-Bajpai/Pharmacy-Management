from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import product
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate
from django.contrib.auth import login 
from django.contrib.auth import logout 

# Create your views here.
def index(request):
    Products = product.objects.all()
    return render(request, 'home.html' )


def about(request):
    return render(request, 'about.html') 


def login_call(request):
    if request.method == 'POST':
        user = request.POST[ 'username']
        pass1 = request.POST[ 'pass']

        us = authenticate (username=user, password=pass1 )
        if us :
            login(request, us )
            return render(request, 'userlogin.html')
            return redirect('userlogin')
        else:
            return redirect('login')
    return render(request, 'login.html') 

def logout_call(request):
    logout(request)
    return redirect('login')
    # return render (request , 'store/signup.html')

def signup(request):
    if request.method =='POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2: 
            return redirect('signup')
        my_user = User.objects.create_user(uname,email,pass1)
        my_user.save()
        return redirect('login')
        # print( uname,email , pass1, pass2)
    return render(request, 'signup.html')


def heart(request):
    return render(request, 'heart.html') 

def liver(request):
    return render(request, 'liver.html') 
    
def diabetes(request):
    return render(request, 'diabetes.html') 
    
def skin(request):
    return render(request, 'skininfection.html') 