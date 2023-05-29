from django.urls import path
from . import views

urlpatterns = [

    
    path('monitoreoICM/', views.viewMonitoreoICM, name='monitoreoICM'),
    path('getConections/', views.getConections, name='getConections'),
    path('tablaConexiones/', views.tablaConexiones, name='tablaConexiones'),

]
