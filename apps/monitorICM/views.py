from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def viewMonitoreoICM(request):

    my_dict = {"insert_me": "I am from views.py"}
    return render(request,'monitorICM.html',context=my_dict)
    #return HttpResponse("return cadena")
    #return HttpResponse(template.render())

# Create your views here.
