from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import product
from .Forms import productform,RawProductForm

# Create your views here.

#this is to pure django form
# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == 'POST':
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             #now the data is good
#             print(my_form.cleaned_data)
#             product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     my_form = RawProductForm(request.POST)
#     context = {
#         'form': my_form
#     }
#     return render(request, 'Product/create.html',context)

#This is to raw html form
# def product_create_view(request):
#     # print(request.GET)
#     # print(request.POST)
#     if request.method=='POST': 
#         my_new_title=request.POST.get('title')
#         print(my_new_title)
#     context = {}
#     return render(request, 'Product/create.html',context)

#This is with create_ini, Django modelo forms
# def product_create_view(request):
#     form = productform(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = productform()

#     context = {
#         'form':form
#     }
#     return render(request, 'Product/create.html',context)
    

def product_detail_view(request,my_id):
    obj = product.objects.get(id=my_id)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description
    # }
    context = {
        'object':obj
    }
    return render(request, 'Product/detail.html',context)


# Initial values for form

def reder_initial_data(request):
    
    initial_data = {
        'title': 'My this awesome title'
    }
    obj = product.objects.get(id=1)
    form = RawProductForm(request.POST or None,initial=initial_data)
    if form.is_valid():
        form.save()
    context = {
        'form':form
    }
    return render(request, 'Product/create.html',context)

def dynamic_lookup_view(request,my_id):
    #obj = product.objects.get(id=my_id)
    obj = get_object_or_404(product,id=my_id)
    # try:
    #     obj = product.objects.get(id=my_id)
    # except product.DoesNotExist:
    #     raise Http404
    context = {
        'object':obj
    }
    return render(request, 'Product/detail_dl.html',context)

def product_delete_view(request,my_id):
    obj = get_object_or_404(product,id=my_id)
    #POST request
    if request.method == 'POST':
        #confirm delete
        obj.delete()
        return redirect('../../../')
    context = {
        'object':obj
    }
    return render(request, 'Product/delete.html',context)

def product_list_view(request):
    queryset = product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'Product/list.html',context)