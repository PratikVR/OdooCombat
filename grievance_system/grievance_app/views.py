from django.shortcuts import render, redirect
from grievance_app.models import * 
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login(request):
    if request.method == 'POST':
        user_email = request.POST.get('user_email')
        password = request.POST.get('password')
        print(user_email)
        print(password)

        user = authenticate(email=user_email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/emp_home')
    return render(request, 'login.html')

def emp_home(request):

    return render(request, 'emp_home.html')
