from django.contrib import admin
from .models import Artesanias, Banners, Contacto

# Register your models here.




class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated','id')
   
admin.site.register(Artesanias,AdministrarModelo)




class AdministrarModelobanners(admin.ModelAdmin):
    readonly_fields = ('created', 'updated','id')
   
admin.site.register(Banners,AdministrarModelobanners)



class AdministrarContacto(admin.ModelAdmin):
    list_display = ('id','mensaje')
    readonly_fields=('created','id')
    search_fields =('id','created')
    date_hierarchy = 'created'


admin.site.register(Contacto, AdministrarContacto)