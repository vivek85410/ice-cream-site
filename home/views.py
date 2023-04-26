from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import contact
#create your views here.
def index(request):
    
    return render(request,'index.html')

def services(request):
    #return HttpResponse("this is services")
    
    return render(request,'services.html')

def About(request):
   #return HttpResponse("welcome to my ice cream centre we have many types of ice creams.")
   return render(request,'About.html')
 
 
def contact(request): 
     #return HttpResponse("feel free to contact on email : singhvivek49966@gmail.com")
    if request.method == "POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        desc=request.POST.get("desc")
        form=contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        form.save()    
    return render(request,'contact.html')
  

