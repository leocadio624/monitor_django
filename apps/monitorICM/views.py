import os
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from django.conf import settings
from apps.monitorICM.models import Intercarrier
from datetime import datetime

import logging
logger = logging.getLogger(__name__)


"""
* Descripcion: Renderiza el template
* del monitor ICM
* Fecha de la creacion:     18/05/2023
* Author:                   Eduardo Bernal
"""
def viewMonitoreoICM(request):

    my_dict = {"insert_me": "I am from views.py"}
    return render(request,'monitorICM.html',context=my_dict)




"""
* Descripcion: Se agrega log de para cuando 
* no se encuentra el archivo
* Fecha de la creacion:     28/05/2023
* Author modificacion:      Eduardo Bernal
* Descripcion: Renderiza tabla de conexiones
* en una solicitud get
* Fecha de la creacion:     19/05/2023
* Author:                   Eduardo Bernal
"""
def tablaConexiones(request):
    

    try:
        
        f = open(settings.RESULTADO_MONITOREO, "r")
        cadena = f.read()
        cadena = cadena.replace("\n","")
        cadena = cadena.strip()
        cadena = cadena[0:len(cadena)-1]

        cadena = '['+cadena+']'
        conexiones = json.loads(cadena)

        for i in conexiones:

            icm             = Intercarrier.objects.filter(nombre = i['ICM'], ip = i['IP']).first()
            date_time_obj   = datetime.strptime(i['FECHA'] + ' ' + i['HORA'], '%Y-%m-%d %H:%M:%S')

            icm.fecha_conexion = date_time_obj
            icm.conexiones = int(i['CON'])
            icm.save()

    except:

        now = datetime.now()
        date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
        logger.warning('Error al acceder al archivo de conexiones '+date_time_str+'')
        

    icms = Intercarrier.objects.all()
    contexto = {'conexiones' : icms}
    
    return render(request,'tb_conexciones.html',context = contexto)



    
    




"""
* Descripcion: Realiza una solicitud post
* Fecha de la creacion:     19/05/2023
* Author:                   Eduardo Bernal
"""
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

def handler404(request, exception):
    return render(request, "not_found.html")


