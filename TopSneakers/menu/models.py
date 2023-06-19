from django.db import models

# Create your models here.
class Detalle(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    cantidad_detalle = models.IntegerField(blank=False, verbose_name='Cantidad detalle')
    subtotal_detalle = models.IntegerField(blank=False, verbose_name='Subtotal detalle')

    def __str__(self):
        return str(self.id_detalle)
    

class Compra(models.Model):
    id_compra = models.AutoField(primary_key=True)
    detalle = models.ForeignKey(Detalle, on_delete=models.CASCADE, related_name='compras')
    f_compra = models.DateField(blank=False, verbose_name='Fecha de compra')
    f_retiro = models.DateField(blank=False, verbose_name='Fecha retiro')
    estado_compra = models.CharField(max_length=40, blank=False, verbose_name='Estado de la compra')
    total = models.IntegerField(blank=False, verbose_name='Total de la compra')
    carrito_compra = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id_compra)

    
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    rut_usuario = models.IntegerField(blank=False, verbose_name='Ingrese su rut')
    nombre_usuario = models.CharField(max_length=20, blank=False, verbose_name='Ingrese su nombre')
    apellido_usuario = models.CharField(max_length=20, blank=False, verbose_name='Ingrese su apellido')
    correo_usuario = models.EmailField(max_length=40, blank=False, verbose_name='Ingrese su correo')
    contraseña_usuario = models.CharField(max_length=40, blank=False)
    respuesta_usuario = models.CharField(max_length=150, blank=False, verbose_name='Respuesta', default='default value')

    def __str__(self):
        return str(self.rut_usuario)

    
class Rol(models.Model):
    id_rol = models.OneToOneField(Usuario, primary_key=True, on_delete=models.CASCADE)
    nombre_rol = models.CharField(max_length=50, blank=False, verbose_name='Nombre Rol')

    def __str__(self):
        return self.nombre_rol

    
class Pregunta(models.Model):
    id_pregunta = models.OneToOneField(Usuario, primary_key=True, on_delete=models.CASCADE)
    nombre_pregunta = models.CharField(max_length=100, blank=False, verbose_name='Pregunta')

    def __str__(self):
        return self.nombre_pregunta

class CategoriaProd(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name="categoria"
        verbose_name_plural="categorias"

    def __str__(self):
        return self.nombre

class Producto (models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='menu')
    descripcion_producto = models.CharField(max_length=150, blank=False, verbose_name='Descripcion producto')
    talla_producto = models.IntegerField(blank=False, verbose_name='Talla de producto')
    stock_producto = models.IntegerField(blank=False, verbose_name='Stock producto')
    precio_producto = models.IntegerField(blank=False, verbose_name='Precio producto')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="producto"
        verbose_name_plural="productos"
