from django.db import models

# Create your models here.
from django.db import models

class Intercarrier(models.Model):

    id = models.AutoField(primary_key = True)
    nombre          = models.CharField('Nombre del intercarrier', max_length = 50, blank = False, null = False)
    ip              = models.CharField('Ip a la que se conecta', max_length = 50, blank = False, null = False)
    fecha_conexion  = models.DateTimeField('Fecha en la que se realiza la conexion', auto_now = False, auto_now_add = False)
    conexiones      = models.IntegerField('Numero de conexiones', blank = False, null = False)

    class Meta:
        verbose_name = 'Intercarrier'
        verbose_name_plural = 'Intercarriers'

    def __str__(self):
        return self.nombre
