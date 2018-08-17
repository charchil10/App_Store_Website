from django.shortcuts import render
#from . import urls

def basic_home_page(request):
    return render(request, 'home.html')
