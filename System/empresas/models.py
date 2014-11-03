from django.db import models

class Empresa(models.Model):
	nombre = models.CharField(max_length = 140)
	direccion = models.CharField(max_length = 250)

	def __unicode__(self): 
		return self.nombre