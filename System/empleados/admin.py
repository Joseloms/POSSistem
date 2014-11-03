from django.contrib import admin
from .models import Departamento,Empleado,Empleado2Equipos
#from equipos.models import Equipo

class EquipoInline(admin.TabularInline):
	model = Empleado.equipos.through
	extra = 1

class DepartamentoAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')
	list_filter = ('nombre','empresa',)
	search_fields = ('nombre',)


class EmpleadoAdmin(admin.ModelAdmin):	
	list_display = ('id','user','departamento','direccion','telefono',)
	list_display_links = ('user',) 
	list_filter = ('departamento',)
	list_per_page = 10
	search_fields = ('nombre','direccion','telefono')
	raw_id_fields = ('user','departamento')
	#filter_horizontal = ("equipos",)
	inlines = [EquipoInline]
	fields = ('user','departamento','direccion','telefono',)
	#list_editable = ('email','telefono',)
	

	#Cliente.allow_tags = Trueclass 

class Empleado2EquiposAdmin(admin.ModelAdmin):
	pass



admin.site.register(Empleado2Equipos,Empleado2EquiposAdmin)
admin.site.register(Departamento,DepartamentoAdmin)
admin.site.register(Empleado,EmpleadoAdmin)