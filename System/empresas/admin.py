from django.contrib import admin
from .models import Empresa

class EmpresaAdmin(admin.ModelAdmin):	
	list_display = ('id','nombre','direccion',)
	list_display_links = ('nombre',) 
	#list_filter = ('tipo','prospecto',)
	#list_per_page = 10
	search_fields = ('nombre','','')
	#list_editable = ('email','telefono',)
	

	#Cliente.allow_tags = True

admin.site.register(Empresa,EmpresaAdmin)

