from django.db import models

# Create your models here.
from django.db import models


class TipoMueble(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion_tipo = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.descripcion_tipo})"


class Mueble(models.Model):
    codigo = models.CharField(max_length=100, unique=True)
    alto = models.IntegerField()
    ancho = models.IntegerField()
    fondo = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True)
    tipo_mueble = models.ForeignKey(TipoMueble, on_delete=models.PROTECT)

    def __str__(self):
        return self.codigo


class Imagen(models.Model):
    url = models.CharField(max_length=255)
    descripcion_imagen = models.CharField(max_length=200, blank=True)
    mueble = models.ForeignKey(
        Mueble, on_delete=models.CASCADE, related_name='imagenes')

    def __str__(self):
        return f"Imagen de {self.mueble.codigo}"


class Ubicacion(models.Model):
    pasillo = models.CharField(max_length=45)
    columna = models.IntegerField()
    nivel = models.IntegerField()
    descripcion = models.CharField(max_length=150, blank=True)

    class Meta:
        unique_together = ('pasillo', 'columna', 'nivel')
        ordering = ['pasillo', 'columna', 'nivel']

    def __str__(self):
        return f"{self.pasillo} - Col {self.columna} - Niv {self.nivel}"


class Movimiento(models.Model):
    mueble = models.ForeignKey(Mueble, on_delete=models.CASCADE)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.PROTECT)
    fecha_entrada = models.DateTimeField()
    fecha_salida = models.DateTimeField(null=True, blank=True)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.cantidad} x {self.mueble.codigo} en {self.ubicacion}"
