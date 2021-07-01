from django.shortcuts import redirect, render
from .models import product, about_us, contact, subscribe
from django.contrib import messages

# Create your views here.
def home(request):
    all_products = product.objects.all()

    contaxt = {
        'all_products': all_products
    }
    return render(request, 'index.html', contaxt)

def aboutus(request):
    return render(request, 'about.html')

def furnitures(request):
    all_products = product.objects.all()

    contaxt = {
        'all_products': all_products
    }
    return render(request, 'furniture.html', contaxt)

def blog(request):
    return render(request, 'blog.html')

def contactus(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email2 = request.POST['email']
        message = request.POST['message']

        if len(name) < 2 or len(phone) < 10 or len(email2) < 5 or len(message) < 4:
            return redirect('contact')
        
        else:
            info = contact(name=name, phone=phone, e_mail=email2, message=message)
            info.save()

            return redirect('home')
    return render(request, 'contact.html')