from django.contrib import admin
from django.urls import path, include

from .views import test, stayloyal, sobrenosotrosadmin, sobrenosotros, registrarse, pumasnea, pu_4, pu_3, pu_2, pu_1, productosadmin,productos, privacidad, perfil, perfiladmin, pago, nikesnea, menuadmin, jordansmoke, jordanair1mid, iniciosesion, inicioadmin, histoordenes, envioypago, elegir, contactosadmin, contactanos, carritoadmin, carrito, airforce, adidassnea, ad_4, ad_3, ad_2, ad_1, modificar, recuperar,admin
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('test/',views.test, name='test'),
    path('stayloyal/',views.stayloyal, name="stayloyal"),
    path('sobrenosotrosadmin/',views.sobrenosotrosadmin, name='sobrenosotrosadmin'),
    path('sobrenosotros/',views.sobrenosotros, name='sobrenosotros'),
    path('registrarse/',views.registrarse, name='registrarse'),
    path('pumasnea/',views.pumasnea, name='pumasnea'),
    path('pu_4/',views.pu_4, name='pu_4'),
    path('pu_3/',views.pu_3, name='pu_3'),
    path('pu_2/',views.pu_2, name='pu_2'),
    path('pu_1/',views.pu_1, name='pu_1'),
    path('productosadmin/',views.productosadmin, name='productosadmin'),
    path('productos/',views.productos, name='productos'),
    
    path('privacidad/',views.privacidad, name='privacidad'),
    path('perfil/',views.perfil, name='perfil'),
    path('perfiladmin/',views.perfiladmin, name='perfiladmin'),
    path('pago/',views.pago, name='pago'),
    path('nikesnea/',views.nikesnea, name='nikesnea'),
    path('menuadmin/',views.menuadmin, name='menuadmin'),
    path('jordansmoke/',views.jordansmoke, name='jordansmoke'),
    path('jordanair1mid/',views.jordanair1mid, name='jordanair1mid'),
    path('',views.iniciosesion, name='iniciosesion'),
    path('inicioadmin/',views.inicioadmin, name='inicioadmin'),
    path('histoordenes/',views.histoordenes, name='histoordenes'),
    path('envioypago/',views.envioypago, name='envioypago'),
    path('elegir/',views.elegir, name='elegir'),
    path('contactosadmin/',views.contactosadmin, name='contactosadmin'),
    path('contactanos/',views.contactanos, name='contactanos'),
    path('carritoadmin/',views.carritoadmin, name='carritoadmin'),
    path('carrito/',views.carrito, name='carrito'),
    path('airforce/',views.airforce, name='airforce'),
    path('modificar/',views.modificar, name='modificar'),
    path('adidassnea/',views.adidassnea, name='adidassnea'),
    path('ad_4/',views.ad_4, name='ad_4'),
    path('ad_3/',views.ad_3, name='ad_3'),
    path('ad_2/',views.ad_2, name='ad_2'),
    path('ad_1/',views.ad_1, name='ad_1'), 
    path('recuperar/',views.recuperar, name='recuperar'),  
    path('admin/',views.admin, name='admin'), 
    path('carro/',include('carro.urls'))

    
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)