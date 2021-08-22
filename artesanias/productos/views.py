from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Banners, Artesanias, Contacto
from .forms import ContactoForm
from django.contrib import messages
# Create your views here.
def principal(request):
    banners=Banners.objects.filter(nombre="bannerprincipal")
    return render(request, "productos/index.html",{'banners':banners})


def nosotros(request):
    banners = Banners.objects.filter(nombre="bannerquienessomos")
    juan = Banners.objects.filter(nombre="Juan Manuel")
    edgar = Banners.objects.filter(nombre="Edgar Acosta")
    jose = Banners.objects.filter(nombre="José Avimelec")
    abraham = Banners.objects.filter(nombre="Abraham Vieyra")
    return render(request, "productos/nosotros.html",{'banners':banners,'juan':juan,'edgar':edgar,'jose':jose,'abraham':abraham})


def contacto(request):
    banners = Banners.objects.filter(nombre="bannercontacto")
    return render(request, "productos/contacto.html",{'banners':banners})


def uruapan(request):
    banners = Banners.objects.filter(nombre="banneruruapan")
    artesania = Artesanias.objects.filter(nombre="Guitarra Acústica")
    artesaniados = Artesanias.objects.filter(nombre="Máscaras artesanales")
    artesaniatres = Artesanias.objects.filter(nombre="Jarrones Alfareria")
    artesaniacuatro = Artesanias.objects.filter(nombre="Elegantes Rebozos")
    artesaniacinco = Artesanias.objects.filter(nombre="Gabanes")
    artesaniaseis = Artesanias.objects.filter(nombre="Manteles")
    return render(request, "productos/uruapan.html",{'banners':banners,'artesania':artesania,'artesaniados':artesaniados,'artesaniatres':artesaniatres,'artesaniacuatro':artesaniacuatro,'artesaniacinco':artesaniacinco,'artesaniaseis':artesaniaseis})


def patzcuaro(request):
    banners = Banners.objects.filter(nombre="bannerpatzcuaro")
    artesania = Artesanias.objects.filter(nombre="Sombrero Chuspas")
    artesaniados = Artesanias.objects.filter(nombre="Muebles y Figuras de animales")
    artesaniatres = Artesanias.objects.filter(nombre="Figuras de diablitos")
    artesaniacuatro = Artesanias.objects.filter(nombre="Mascaras de madera")
    artesaniacinco = Artesanias.objects.filter(nombre="Juguetes")
    artesaniaseis = Artesanias.objects.filter(nombre="Ollas")
    return render(request, "productos/patzcuaro.html",{'banners':banners,'artesania':artesania,'artesaniados':artesaniados,'artesaniatres':artesaniatres,'artesaniacuatro':artesaniacuatro,'artesaniacinco':artesaniacinco,'artesaniaseis':artesaniaseis})


def quiroga(request):
    banners = Banners.objects.filter(nombre="bannerquiroga")
    artesania = Artesanias.objects.filter(nombre="Piña de barro")
    artesaniados = Artesanias.objects.filter(nombre="Platos artesanales")
    artesaniatres = Artesanias.objects.filter(nombre="Gallina Huevara")
    artesaniacuatro = Artesanias.objects.filter(nombre="Tequileros Decorados")
    artesaniacinco = Artesanias.objects.filter(nombre="Cazos")
    artesaniaseis = Artesanias.objects.filter(nombre="Titeres")
    return render(request, "productos/quiroga.html",{'banners':banners,'artesania':artesania,'artesaniados':artesaniados,'artesaniatres':artesaniatres,'artesaniacuatro':artesaniacuatro,'artesaniacinco':artesaniacinco,'artesaniaseis':artesaniaseis})


def registrar(request):
    banners = Banners.objects.filter(nombre="bannercontacto")
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
                form.save()
                return render(request,"productos/gracias.html",{'banners':banners})
    form = ContactoForm()
    return render(request, 'productos/contacto.html',{'form':form})

def gracias(request):
    banners = Banners.objects.filter(nombre="bannercontacto")
    return render(request, 'productos/gracias.html',{'banners':banners})



def acustica(request):
    banners = Banners.objects.filter(nombre="Banner Uruapan productos")
    artesanias=Artesanias.objects.filter(nombre="Guitarra Acústica")
    return render(request, "productos/acustica.html",{'artesania':artesanias,'banners':banners})

def cazos(request):
    banners = Banners.objects.filter(nombre="Banner Quiroga productos")
    artesanias=Artesanias.objects.filter(nombre="Cazos")
    return render(request, "productos/cazos.html",{'artesanias':artesanias,'banners':banners})

def mascarasmadera(request):
    banners = Banners.objects.filter(nombre="Banner Patzcuaro productos")
    artesanias=Artesanias.objects.filter(nombre="Mascaras de madera")
    return render(request, "productos/mascarasmadera.html",{'artesanias':artesanias,'banners':banners})    

def cazuelas(request):
    banners = Banners.objects.filter(nombre="Banner Uruapan productos")
    artesanias=Artesanias.objects.filter(nombre="Guitarra Acústica")
    return render(request, "productos/cazuelas.html")

def figuras(request):
    banners = Banners.objects.filter(nombre="Banner Patzcuaro productos")
    artesanias=Artesanias.objects.filter(nombre="Figuras de diablitos")
    return render(request, "productos/figuras.html",{'artesanias':artesanias,'banners':banners})

def gallina(request):
    banners = Banners.objects.filter(nombre="Banner Quiroga productos")
    artesanias=Artesanias.objects.filter(nombre="Gallina Huevara")
    return render(request, "productos/gallina.html",{'artesanias':artesanias,'banners':banners})

def platoartesanal(request):
    banners = Banners.objects.filter(nombre="Banner Quiroga productos")
    artesanias=Artesanias.objects.filter(nombre="Platos artesanales")
    return render(request, "productos/platoartesanal.html",{'artesanias':artesanias,'banners':banners})

def pinabarro(request):
    banners = Banners.objects.filter(nombre="Banner Quiroga productos")
    artesanias=Artesanias.objects.filter(nombre="Piña de barro")
    return render(request, "productos/pinabarro.html",{'artesanias':artesanias,'banners':banners})

def vasostequileros(request):
    banners = Banners.objects.filter(nombre="Banner Quiroga productos")
    artesanias=Artesanias.objects.filter(nombre="Tequileros Decorados")
    return render(request, "productos/vasostequileros.html",{'artesanias':artesanias,'banners':banners})



def gabanes(request):
    banners = Banners.objects.filter(nombre="Banner Uruapan productos")
    artesanias=Artesanias.objects.filter(nombre="Gabanes")
    return render(request, "productos/gabanes.html",{'artesanias':artesanias,'banners':banners})


def jarrones(request):
    banners = Banners.objects.filter(nombre="Banner Uruapan productos")
    artesanias=Artesanias.objects.filter(nombre="Jarrones Alfareria")
    return render(request, "productos/jarrones.html",{'artesanias':artesanias,'banners':banners})


def jorongos(request):
    banners = Banners.objects.filter(nombre="Banner Uruapan productos")
    artesanias=Artesanias.objects.filter(nombre="Jarrones Alfareria")
    return render(request, "productos/jorongos.html",{'artesanias':artesanias,'banners':banners})

def jueguetes(request):
    banners = Banners.objects.filter(nombre="Banner Patzcuaro productos")
    artesanias=Artesanias.objects.filter(nombre="Juguetes")
    return render(request, "productos/juguetes.html",{'artesanias':artesanias,'banners':banners})

def manteles(request):
    banners = Banners.objects.filter(nombre="Banner Uruapan productos")
    artesanias=Artesanias.objects.filter(nombre="Manteles")
    return render(request, "productos/manteles.html",{'artesanias':artesanias,'banners':banners})


def mascara(request):
    banners = Banners.objects.filter(nombre="Banner Uruapan productos")
    artesanias=Artesanias.objects.filter(nombre="Máscaras artesanales")
    return render(request, "productos/mascara.html",{'artesanias':artesanias,'banners':banners})


def muebles(request):
    banners = Banners.objects.filter(nombre="Banner Patzcuaro productos")
    artesanias=Artesanias.objects.filter(nombre="Muebles y Figuras de animales")
    return render(request, "productos/muebles.html",{'artesanias':artesanias,'banners':banners})


def ollas(request):
    banners = Banners.objects.filter(nombre="Banner Patzcuaro productos")
    artesanias=Artesanias.objects.filter(nombre="Ollas")
    return render(request, "productos/ollas.html",{'artesanias':artesanias,'banners':banners})

def rebozos(request):
    banners = Banners.objects.filter(nombre="Banner Uruapan productos")
    artesanias=Artesanias.objects.filter(nombre="Elegantes Rebozos")
    return render(request, "productos/rebozos.html",{'artesanias':artesanias,'banners':banners})

def gabanes(request):
    banners = Banners.objects.filter(nombre="Banner Uruapan productos")
    artesanias=Artesanias.objects.filter(nombre="Gabanes")
    return render(request, "productos/rebozos.html",{'artesanias':artesanias,'banners':banners})

def titeres(request):
    banners = Banners.objects.filter(nombre="Banner Quiroga productos")
    artesanias=Artesanias.objects.filter(nombre="Titeres")
    return render(request, "productos/titeres.html",{'artesanias':artesanias,'banners':banners})

def sombreros(request):
    banners = Banners.objects.filter(nombre="Banner Patzcuaro productos")
    artesanias=Artesanias.objects.filter(nombre="Sombrero Chuspas")
    return render(request, "productos/sombreros.html",{'artesanias':artesanias,'banners':banners})





































