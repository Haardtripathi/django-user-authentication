from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login

def home(request):
    return render(request,'home.html')

def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")

        password = request.POST.get("password")
        user=authenticate(username=username, email=email,password=password)    
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            messages.info(request,"Invalid username or info")
            return redirect("login")    
    else:
        return render(request,'login.html')

# Create your views here.
def signup(request):
    if(request.method=="POST"):
        username=request.POST['username']
        email=request.POST['email']
        p1=request.POST['password']
        p2=request.POST['password1']
        if(p1==p2):
            if(User.objects.filter(username=username).exists()):
                messages.info(request,"Username already exists")
                return redirect('signup')
            elif(User.objects.filter(email=email).exists()):
                messages.info(request,"Email already registered")
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username,email=email,password=p1)
                user.save()
                return redirect('home')
        else:
            messages.info(request,"Passwords do not match")
            return redirect('signup')
    else:
        return render(request, 'signup.html')


def logoutUser(request):
    logout(request)
    return redirect("/login")