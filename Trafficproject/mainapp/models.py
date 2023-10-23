from django.db import models

class Usuarios(models.Model):
    nombre = models.CharField(max_length=200)
    correo = models.EmailField(max_length=200)
    telefono = models.CharField(max_length=20)  
    direccion = models.TextField()              

    def __str__(self):
        return self.nombre

class Localidad(models.Model):
    codigo = models.CharField(max_length=100)   
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Señales(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    # aplicacion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class SituacionesRiesgo(models.Model):
    nombre = models.CharField(max_length=200)
    tipo_de_actor_vial = models.CharField(max_length=50) 
    direccion = models.TextField()
    latitud = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)  
    longitud = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    existencia_señales = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

class Estadisticas(models.Model):
    id = models.AutoField(primary_key=True) 
    contenido = models.TextField()       
    tipo_estadistica = models.CharField(max_length=100) 
    responsable = models.CharField(max_length=200, blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
