from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'home/index.html')

def handleSignup(request):
    if request.method == 'POST':
        fName = request.POST['fName']
        lName = request.POST['lName']
        username = request.POST['signupUsername']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        print(fName, lName, username, pass1, pass2)

        myUser = User.objects.create_user(username, email, pass1)
        myUser.first_name = fName
        myUser.last_name = lName
        myUser.save()
        messages.success(request, 'Signed up successfully')
        return redirect('home')

    else:
        return HttpResponse('404 - not found')
    
def handleLogin(request):
    if request.method == 'POST':
        username = request.POST['loginUsername']
        password = request.POST['password']

        user = authenticate(username = username, password = password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully')
            return redirect('home')
        
        else:
            messages.error(request, 'Invalid credentials, please check username & password again!!!')
            return redirect('home')

    return HttpResponse('404 - not found')

def handleLogout(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('home')

