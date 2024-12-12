from django.contrib import auth
from django.shortcuts import render, redirect
from pyexpat.errors import messages
from django.contrib import messages  # Import messages
from .models import *
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.shortcuts import redirect

# Create your views here.

def index(request):
    book = Product.objects.all()

    context = {
        'book': book,
    }
    return render(request, 'index.html', context)




def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        User.objects.create_user(username=username,email=email, password=password)
        return redirect('login/')
    return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Login the user
            messages.success(request, 'You have successfully logged in.')  # Add success message
            return render(request, 'login.html')  # Redirect to the login page (or replace with a home page)
        else:
            messages.error(request, 'Invalid username or password.')  # Add error message
            return render(request, 'login.html')  # Return to login page with error
    return render(request, 'login.html')


def search(request):
    book = Product.objects.all()
    if request.method == 'POST':
        search = request.POST.get('search')

        results = Product.objects.filter(Q(title__icontains=search))
        context = {
            'result': results
        }
        return render(request, 'search.html', context)

    context = {
        'book': book,

    }

    return render(request, 'search.html', context)


def logout_view(request):
    auth.logout(request)  # Logs out the user
    return redirect('login')  # Redirect to the login page or any other page after logout
