from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,"home.html")

def aboutus(request):
    return render(request,"about.html")

def contactus(request):
    return render(request,"contact.html")

def myform(request):
    return render(request,'myform.html')

def process(request):
    print("Welcome")
    print(request.method)
    print(request.POST)
    a = int(request.POST[ 'txt1' ])
    b = int(request.POST[ 'txt2' ])
    c = a + b
    print(c)
    context={
        'aa':a,
        'bb':b,
        'mysum':c,
    }

    return render(request,'ans.html',context)
