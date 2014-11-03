from django.db import models
from marcas.models import Marca

class Unidades(models.Model):
	nombre = models.CharField(max_length = 140, blank = True)

	def __unicode__(self):
		return self.nombre

class Producto(models.Model):
	nombre	= models.CharField(max_length=140)
	slug 	= slug = models.SlugField(max_length=50, unique=True, help_text='Valor unico por producto URL pagina, creado desde nombre.',blank=True,null=True) 
	sku 	= models.CharField(max_length=140,blank=True,null=True)
	es_activo = models.BooleanField(default=True) 
	stock 	= models.IntegerField(blank=True)
	imagen 	= models.ImageField("Imagen Producto", upload_to="images/producto", blank=True, null=True)
	presenatacion = models.CharField(max_length = 140)
	peso 	= models.DecimalField(max_digits=9, decimal_places=2,blank=True,null=True)
	unidad 	= models.ForeignKey(Unidades, blank = True)
	precio 	= models.DecimalField(max_digits=9, decimal_places=2)
	marca 	= models.ForeignKey(Marca, blank = True)
	promocion = models.BooleanField(default=False) 

	def imagen_producto(self):
		return """<img src="%s" style="width:8em;" />""" % self.imagen.url

	imagen_producto.allow_tags = True

	def __unicode__(self): 
		return "%s - %s - %s"% (self.nombre, self.marca, self.presenatacion)