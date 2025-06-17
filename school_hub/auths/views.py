from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('home')  # Replace with your actual home route
    else:
        form = CustomUserCreationForm()
    return render(request, "auths/register.html", {'form': form})

def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')  # Replace with your actual home route
        else:
            messages.error(request, 'Invalid credentials.')
    else:
        form = CustomAuthenticationForm()
    return render(request, "auths/login.html", {'form': form})
