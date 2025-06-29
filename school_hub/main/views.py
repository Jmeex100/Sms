from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'main/home.html')

def contact(request):
    return render(request, 'main/contact.html')

# New views for terms, privacy, and cookies

def terms(request):
    return render(request, 'main/terms.html')

def privacy(request):
    return render(request, 'main/privacy.html')

def cookies(request):
    return render(request, 'main/cookies.html')


# dont  touch up 