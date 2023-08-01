from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    # Your view logic here
    context = {
        'welcome_message': 'Welcome to our website!',
    }
    return render(request, 'home.html', context)