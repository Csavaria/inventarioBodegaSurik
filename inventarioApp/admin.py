from django.contrib import admin
from .models import Imagen, Movimiento, Mueble, TipoMueble, Ubicacion

# Register your models here.
admin.site.register(Imagen)
admin.site.register(Movimiento)
admin.site.register(Mueble)
admin.site.register(TipoMueble)
admin.site.register(Ubicacion)
