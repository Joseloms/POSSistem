from django.contrib import admin
from .models import Equipo

class EquipoAdmin(admin.ModelAdmin):
	list_display = ('id','nombre','modelo','serial')
	list_filter = ('nombre',)
	list_per_page = 10
	search_fields = ('nombre','serial')

admin.site.register(Equipo,EquipoAdmin)
