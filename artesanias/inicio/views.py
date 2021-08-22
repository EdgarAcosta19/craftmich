from django.db import models
from django.shortcuts import render,HttpResponse
from productos.models import Artesanias, Banners
from django.db.models import Q 
# Create your views here.
def principal(request):
    return render(request, "inicio/index.html")

def listar_productos(request):
    check = ""
    banners=Banners.objects.filter(nombre="bannerbuscador")
    busqueda = request.GET.get("buscar")
    artesanias = Artesanias.objects.all()
    check = "no"
  
    if busqueda:
        artesanias = Artesanias.objects.filter(
           Q(nombre__icontains = busqueda) |
           Q(municipio__icontains = busqueda)|
           Q(descripcion__icontains = busqueda)
        ).distinct()  
        check = "listo"
    if artesanias.exists():
        check = "listo"
    else:
        check= "no encontrado"  

    print(check)      
    return render(request, "inicio/encabezado.html",{'artesanias':artesanias,'comprobacion':check,'banners':banners})




def nosotros(request):
    return render(request, "inicio/nosotros.html")


def contacto(request):
    return render(request, "inicio/contacto.html")


def uruapan(request):
    return render(request, "inicio/uruapan.html")


def patzcuaro(request):
    return render(request, "inicio/patzcuaro.html")


def quiroga(request):
    return render(request, "inicio/quiroga.html")


def acustica(request):
    return render(request, "inicio/acustica.html")




def cazos(request):
    return render(request, "inicio/cazos.html")

def mascarasmadera(request):
    return render(request, "inicio/mascarasmadera.html")    

def cazuelas(request):
    return render(request, "inicio/cazuelas.html")

def figuras(request):
    return render(request, "inicio/figuras.html")

def gallina(request):
    return render(request, "inicio/gallina.html")

def platoartesanal(request):
    return render(request, "inicio/platoartesanal.html")

def pinabarro(request):
    return render(request, "inicio/pinabarro.html")

def vasostequileros(request):
    return render(request, "inicio/vasostequileros.html")



def gabanes(request):
    return render(request, "inicio/gabanes.html")


def jarrones(request):
    return render(request, "inicio/jarrones.html")


def jorongos(request):
    return render(request, "inicio/jorongos.html")

def jueguetes(request):
    return render(request, "inicio/juguetes.html")

def manteles(request):
    return render(request, "inicio/manteles.html")


def mascara(request):
    return render(request, "inicio/mascara.html")


def muebles(request):
    return render(request, "inicio/muebles.html")


def ollas(request):
    return render(request, "inicio/ollas.html")

def rebozos(request):
    return render(request, "inicio/rebozos.html")

def titeres(request):
    return render(request, "inicio/titeres.html")

def sombreros(request):
    return render(request, "inicio/sombreros.html")





































