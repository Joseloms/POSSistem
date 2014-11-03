from django.db import models
from empleados.models import Empleado

class Tipo_Servicio(models.Model):
	nombre = models.CharField(max_length = 140, blank=True)

	def __unicode__(self): 
		return self.nombre

class Servicio(models.Model):
	tipo = models.ForeignKey(Tipo_Servicio,blank=True)
	fecha_cracion = models.DateTimeField(auto_now_add=True)
	empleado = models.ForeignKey(Empleado,blank=True)
	fecha_a_agendar = models.DateTimeField()
	descripcion = models.TextField(blank=True)
	observaciones = models.TextField(blank=True)
	fecha_terminacion = models.DateTimeField(auto_now=True)

	def __unicode__(self): 
		return "%s - %s"% (self.tipo, self.fecha_cracion)


