from django.db import models
from django.contrib.auth.models import User
from empresas.models import Empresa
from equipos.models import Equipo

class Departamento(models.Model):
	nombre = models.CharField(max_length=140)
	empresa = models.ForeignKey(Empresa, blank=True)

	def __unicode__(self): 
		return "%s - %s"% (self.nombre, self.empresa)

class Empleado(models.Model):
	user = models.ForeignKey(User, unique=True)
	departamento = models.ForeignKey(Departamento, blank=True, null=True)
	direccion = models.CharField(max_length=250, blank=True)
	telefono = models.PositiveIntegerField(null=True, blank=True)
	equipos = models.ManyToManyField(Equipo, symmetrical=True,  blank=True)

	def __unicode__(self): 
		return unicode(self.user)

class Empleado2Equipos(models.Model):
    emplado = models.ForeignKey(Empleado)
    equipos = models.ForeignKey(Equipo)

    class Meta:
        unique_together = ('emplado', 'equipos')

