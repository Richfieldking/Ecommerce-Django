from django.shortcuts import render



def home(request):

   # if request.user.is_authenticated():
    username_is = "Richfield"
    context = {"username_is": username_is}
   # else:
   #     context = {"username_is": "unknown"}

    templates = "products/base.html"
    return render(request, templates, context)
