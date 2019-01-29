from django.shortcuts import render
from .models import Product



def home(request):

    if request.method=='POST':
           username_is = "Richfield"
           context = {"username_is": request.user}
    else:
           context = {"username_is": request.user}

    templates = "products/base.html"
    return render(request, templates, context)

def all(request):
       
       products= Product.objects.all()
       context = {
          'products':products

       }
       template = "products/all.html"
       return render(request, template, context)