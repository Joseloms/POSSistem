from django.db import models
from empresas.models import Empresa

class Marca(models.Model):
	nombre = models.CharField(max_length=140)
	logo = models.ImageField("Logo Marca", upload_to="images/", blank=True, null=True)
	empresa = models.ForeignKey(Empresa, blank=True)

	def imagen_logo(self):
		return """<img src="%s" width="200px" />""" % self.logo.url

	imagen_logo.allow_tags = True

	#def image_logo(self):
	#	if self.logo:
	#		return """<img src="%s" />""" % self.logo.url
	#	else:
	#		return '(Sin imagen)'
#
#		image_logo.short_description = 'Thumb'
#		image_logo.allow_tags = True

	def __unicode__(self): 
		return  self.nombre

