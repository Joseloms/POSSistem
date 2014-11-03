from django.db import models
#from empleados.models import Empleado

class Equipo(models.Model):
	nombre = models.CharField(max_length = 140)
	modelo = models.CharField(max_length = 140)
	serial = models.CharField(max_length = 140)
	#empleado = models.ForeignKey(Empleado, blank=True, null=True)


	def __unicode__(self): 
		return "%s - %s"% (self.nombre, self.modelo)