from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact

def index(request):

    #context is a set of variable 
    context = {
        'variablename': 'this is the value of the variable'
    }
    return render(request, 'index.html', context)
    #return HttpResponse("This is home page")
def about(request):
    return render(request, 'about.html')
    #return HttpResponse("This is about page")
def services(request):
    return render(request, 'services.html')
    #return HttpResponse("This is services page")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, phone=phone, email=email, desc=desc, date=datetime.today() )
        contact.save()
        
    return render(request, 'contact.html')
    #return HttpResponse("This is contact page")