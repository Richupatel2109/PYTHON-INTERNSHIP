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
    FirstName = request.POST[ 'txt1' ]
    MiddleName = request.POST[ 'txt2' ]
    LastName = request.POST[ 'txt3' ]
    Collage = request.POST[ 'txt4' ]
    Email = request.POST[ 'txt5' ]
    Age = request.POST[ 'txt6' ]
    Roll_No = request.POST[ 'txt7' ]
    Branch = request.POST[ 'txt8']
    Contact_No = request.POST[ 'txt9' ]
    Country = request.POST[ 'txt10' ]
    State = request.POST[ 'txt11' ]

    context={
        'FirstName':FirstName,
        'MiddleName':MiddleName,
        'LastName':LastName,
        'Collage':Collage,
        'Email':Email,
        'Age':Age,
        'Roll_No':Roll_No,
        'Branch':Branch,
        'Contact_No':Contact_No,
        'Country':Country,
        'State':State,
    }

    return render(request,'ans.html',context)
