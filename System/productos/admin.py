from django.contrib import admin
from .models import Producto, Unidades

@admin.register(Unidades)
class UnidadesAdmin(admin.ModelAdmin):
	list_display 	= ('id','nombre')
	list_editable	= ('nombre',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):	
	fields 			= ('nombre', 'slug','sku','es_activo','stock','imagen',('presenatacion','peso','unidad'),('precio','promocion'), 'marca')
	list_display 	= ('id','nombre', 'imagen_producto','presenatacion','precio', 'marca','es_activo','promocion')
	#list_display_links = ('nombre') 
	list_filter 	= ('presenatacion','marca')
	list_per_page 	= 10
	search_fields 	= ('nombre','','')
	list_editable 	= ('nombre','precio','marca',)

	prepopulated_fields = {'slug' : ('nombre','presenatacion','marca')} 



	

	#Cliente.allow_tags = True

#admin.site.register(Unidades,UnidadesAdmin)
#admin.site.register(Producto,ProductoAdmin)