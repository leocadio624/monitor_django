from django.urls import path
from . import views

urlpatterns = [
    path('monitoreoICM/', views.viewMonitoreoICM, name='monitoreoICM'),
]
