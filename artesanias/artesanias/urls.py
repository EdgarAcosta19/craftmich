"""artesanias URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inicio import views as p
from productos import views
from django.conf import  settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.principal, name="Pagina principal"), # principal
    path('Contacto/',views.contacto, name="Contacto"), # contacto
    path('Nosotros/',views.nosotros ,name="Nosotros"), #quienes somos
    path('registrar/',views.registrar,name="Registrar"),
    path('artesania/',p.listar_productos,name="artesania"),
    path('gracias/',views.gracias,name="Gracias"),
    path('Uruapan/',views.uruapan ,name="Uruapan"), #uruapan
    path('Patzcuaro/',views.patzcuaro ,name="Patzcuaro"), #patzcuaro
    path('Quiroga/',views.quiroga ,name="Quiroga"), #quiroga
    path('Acustica/',views.acustica ,name="Acustica"), # p-uruapan
    path('Cazos/',views.cazos ,name="Cazos"), # p- Quiroga
    path('Figuras/',views.figuras ,name="Figuras"), #Patzcuaro
    path('Gabanes/',views.gabanes ,name="Gabanes"), # p-uruapan
    path('Gallina/',views.gallina ,name="Gallina"), # P-quiroga
    path('Jarrones/',views.jarrones ,name="Jarrones"), # p-uruapan
    path('Juguetes/',views.jueguetes ,name="Juguetes"), #Patzcuaro ---falta
    path('Manteles/',views.manteles ,name="Manteles"), #P-uruapan
    path('Mascara/',views.mascara ,name="Mascara"), #P-uruapan
    path('Gabanes/',views.gabanes ,name="Gabanes"),#P-uruapan
    path('Mascarasmadera/',views.mascarasmadera ,name="Mascarasmadera"), #Patcuaro
    path('Muebles/',views.muebles,name="Muebles"), # Patzcuaro
    path('Ollas/',views.ollas,name="Ollas"), #Patzcuaro --- patzcuaro
    path('Pinabarro/',views.pinabarro,name="Pinabarro"), #P-quroga
    path('Platoartesanal/',views.platoartesanal,name="Platoartesanal"), #P-quiroga
    path('Rebozos/',views.rebozos,name="Rebozos"),#P-uruapan
    path('Sombreros/',views.sombreros,name="Sombreros"), # Patzcuaro
    path('Titeres/',views.titeres,name="Titeres"), # p- Quiroga
    path('Vasostequileros/',views.vasostequileros,name="Vasotequileros"),#P-quiroga

]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
             document_root=settings.MEDIA_ROOT)
