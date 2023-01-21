from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request,*args,**kwargs):
    print(args,kwargs)
    print(request.user)
    return render(request,"home.html",{}) # string of HTML

def contact_view(*args,**kwargs):
    return HttpResponse("<h1>Contacts page</h1>")

def about_view(request,*args,**kwargs):
    print(args,kwargs)
    print(request.user)
    return render(request,"about.html",{})

def page1_view(request,*args,**kwargs):
    my_context = {
        'my_text':'This is about us',
        'my_number':123,
        'my_list':[123,456,'abc']
    }
    return render(request,"page1.html",my_context)


