from django.shortcuts import render


# Original untouched views
def home(request):
    return render(request, 'main/home.html')

def contact(request):
    return render(request, 'main/contact.html')

def terms(request):
    return render(request, 'main/terms.html')

def privacy(request):
    return render(request, 'main/privacy.html')

def cookies(request):
    return render(request, 'main/cookies.html')

# New views
def help(request):
    return render(request, 'main/help.html')

def about(request):
    return render(request, 'main/about.html')

def profile(request):
    return render(request, 'main/profile.html')

def events(request):
    return render(request, 'main/events.html')

def resources(request):
    return render(request, 'main/resources.html')