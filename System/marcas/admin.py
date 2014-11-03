from django.contrib import admin
from .models import Marca

class MarcaAdmin(admin.ModelAdmin):	
	list_display = ('id','nombre', 'imagen_logo')
	list_display_links = ('nombre',)
	#list_per_page = 10
	search_fields = ('nombre',)
	#list_editable = ('nombre',)

	#Marca.allow_tags = True

admin.site.register(Marca,MarcaAdmin)

