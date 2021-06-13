from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('HELLO WORLD')

def aboutus(request):
    return HttpResponse('About Us')

def contactus(request):
    return HttpResponse('Contact Us')
