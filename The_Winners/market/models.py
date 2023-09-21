from django.db import models


class Multimedia_Principal(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    video = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.titulo
    


class Tipos_De_Comida_Imagen_Por_Producto(models.Model):
    titulo = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo
    
class Comidas_Imagen_Por_Producto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='imagenes/')
    Pertenece_A = models.ForeignKey(Tipos_De_Comida_Imagen_Por_Producto, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Tipos_De_Comida_Unica_Imagen(models.Model):
    titulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='imagenes/')

    def __str__(self):
        return self.titulo

class Comidas_Unica_Imagen(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.CharField(max_length=100)
    Pertenece_A = models.ForeignKey(Tipos_De_Comida_Unica_Imagen, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    
class Promociones(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='imagenes/')

    def __str__(self):
        return self.titulo



class Mapa(models.Model):
    titulo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='imagenes/')
    latitud = models.CharField(max_length=100)
    longitud = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo


class Contacto(models.Model):
    telefono = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.telefono
    

class Fecha_Partidos(models.Model):
    nombre_en_admin = models.CharField(max_length=100)
    dia = models.IntegerField()
    mes = models.IntegerField()
    año = models.IntegerField()

    def __str__(self):
        return self.nombre_en_admin
    

class Partidos(models.Model):
    fecha_del_partido = models.ForeignKey(Fecha_Partidos, on_delete=models.CASCADE)
    torneo = models.CharField(max_length=100)
    equipo_1 = models.CharField(max_length=100)
    imagen_equipo1 = models.ImageField(upload_to='imagenes/')
    equipo_2 = models.CharField(max_length=100)
    imagen_equipo2 = models.ImageField(upload_to='imagenes/')
    hora = models.CharField(max_length=100)
    
    def __str__(self):
        return self.torneo