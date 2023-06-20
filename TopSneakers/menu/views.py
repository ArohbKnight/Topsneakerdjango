from django.shortcuts import render
from .models import Producto

# Create your views here.
def test(request):
    return render (request,'menu/test.html')

def productos(request):

    productos=Producto.objects.all()

    return render (request,'menu/productos.html',{"productos":productos})

    

def stayloyal(request):
    return render (request,'menu/stayloyal.html')

def sobrenosotrosadmin(request):
    return render (request,'menu/sobrenosotrosadmin.html')

def sobrenosotros(request):
    return render (request,'menu/sobrenosotros.html')

def registrarse(request):
    return render (request,'menu/registrarse.html')

def pumasnea(request):
    return render (request,'menu/pumasnea.html')

def pu_4(request):
    return render (request,'menu/pu_4.html')

def pu_3(request):
    return render (request,'menu/pu_3.html')

def pu_2(request):
    return render (request,'menu/pu_2.html')

def pu_1(request):
    return render (request,'menu/pu_1.html')

def productosadmin(request):
    return render (request,'menu/productosadmin.html')

def privacidad(request):
    return render (request,'menu/privacidad.html')

def perfiladmin(request):
    return render (request,'menu/perfiladmin.html')

def perfil(request):
    return render (request,'menu/perfil.html')

def pago(request):
    return render (request,'menu/pago.html')

def nikesnea(request):
    return render (request,'menu/nikesnea.html')

def menuadmin(request):
    return render (request,'menu/menuadmin.html')

def jordansmoke(request):
    return render (request,'menu/jordansmoke.html')

def jordanair1mid(request):
    return render (request,'menu/jordanair1mid.html')

def iniciosesion(request):
    return render (request,'menu/iniciosesion.html')

def inicioadmin(request):
    return render (request,'menu/inicioadmin.html')

def histoordenes(request):
    return render (request,'menu/histoordenes.html')

def envioypago(request):
    return render (request,'menu/envioypago.html')

def elegir(request):
    return render (request,'menu/elegir.html')

def contactosadmin(request):
    return render (request,'menu/contactosadmin.html')
def contactanos(request):
    return render (request,'menu/contactanos.html') 

def carritoadmin(request):
    return render (request,'menu/carritoadmin.html')
def carrito(request):
    return render (request,'menu/carrito.html')

def airforce(request):
    return render (request,'menu/airforce.html')

def modificar(request):
    return render (request,'menu/modificar.html')

def adidassnea(request):
    return render (request,'menu/adidassnea.html')

def ad_4(request):
    return render (request,'menu/ad_4.html')

def ad_3(request):
    return render (request,'menu/ad_3.html')

def ad_2(request):
    return  render(request,'menu/ad_2.html')

def ad_1(request):
    return render (request,'menu/ad_1.html')

def recuperar(request):
    return render (request,'menu/recuperar.html')
def admin(request):
    return render (request,'menu/admin.html')
