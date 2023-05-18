import os
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from django.conf import settings


def viewMonitoreoICM(request):

    my_dict = {"insert_me": "I am from views.py"}
    return render(request,'monitorICM.html',context=my_dict)
    #return HttpResponse("return cadena")
    #return HttpResponse(template.render())



def tablaConexiones(request):

    """
    f = open(settings.RESULTADO_MONITOREO, "r")
    cadena = f.read()
    cadena = cadena.replace("\n","")
    cadena = cadena.strip()
    cadena = cadena[0:len(cadena)-1]
    
    cadena = '['+cadena+']'
    """
    
    #conexiones = json.loads(cadena)


    #my_dict = {"insert_me": "I am from views.py"}
    contexto = {"conexiones":[{"ICM":"MOVI","IP":"10.14.164.42","CON":"0","FECHA":"2023-05-17","HORA":"15:58:56"},{"ICM":"SYBASE","IP":"74.117.9.62","CON":"5","FECHA":"2023-05-17","HORA":"15:58:56"},{"ICM":"SYNIVERSE","IP":"173.209.200.137","CON":"2","FECHA":"2023-05-17","HORA":"15:58:56"}]}

    return render(request,'tb_conexciones.html',context = contexto)

    #return HttpResponse("return cadena")
    #return HttpResponse(template.render())


# Create your views here.


@csrf_exempt 
def getConections(request):

    

    
    



    """
    """


    if request.method == "POST":

        f = open(settings.RESULTADO_MONITOREO, "r")
        cadena = f.read()
        cadena = cadena.replace("\n","")
        cadena = cadena.strip()
        cadena = cadena[0:len(cadena)-1]
        
        cadena = '['+cadena+']'
        conexiones = json.loads(cadena)
        

        return HttpResponse(json.dumps(conexiones))

        #return JsonResponse(conexiones)

        #return HttpResponse(conexiones)


    #return HttpResponse("return this string")

    """
    print(request.method)

    if request.method == "POST":
        res = requests.get(f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita")
        return JsonResponse(res.json())
    """


