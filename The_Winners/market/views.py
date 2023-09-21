from django.http import HttpResponse
from .models import (
    Multimedia_Principal,
    Tipos_De_Comida_Imagen_Por_Producto,
    Comidas_Imagen_Por_Producto,
    Tipos_De_Comida_Unica_Imagen,
    Comidas_Unica_Imagen,
    Promociones,
    Mapa,
    Contacto,
    Fecha_Partidos,
    Partidos,
)
import json

def data_api(request):


    modelo1_data = Multimedia_Principal.objects.all().values()

    modelo3_data = Tipos_De_Comida_Imagen_Por_Producto.objects.all().values()
    modelo4_data = Comidas_Imagen_Por_Producto.objects.all().values()
    modelo5_data = Tipos_De_Comida_Unica_Imagen.objects.all().values()
    modelo6_data = Comidas_Unica_Imagen.objects.all().values()
    modelo7_data = Promociones.objects.all().values()

    modelo9_data = Mapa.objects.all().values()
    modelo10_data = Contacto.objects.all().values()
    modelo11_data = Fecha_Partidos.objects.all().values()
    modelo12_data = Partidos.objects.all().values()

    data = {
        'Multimedia_Principal': list(modelo1_data),
        'Tipos_De_Comida_Imagen_Por_Producto': list(modelo3_data),
        'Comidas_Imagen_Por_Producto': list(modelo4_data),
        'Tipos_De_Comida_Unica_Imagen': list(modelo5_data),
        'Comidas_Unica_Imagen': list(modelo6_data),
        'Promociones': list(modelo7_data),
        'Mapa': list(modelo9_data),
        'Contacto': list(modelo10_data),
        'Fecha_Partidos': list(modelo11_data),
        'Partidos': list(modelo12_data),
    }

    json_data = json.dumps(data)

    # Crear una respuesta HTTP con los datos y evitar el almacenamiento en caché
    response = HttpResponse(json_data, content_type='application/json')
    response["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response["Pragma"] = "no-cache"
    response["Expires"] = "0"

    return response
