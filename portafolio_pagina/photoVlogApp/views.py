from django.shortcuts import render,  HttpResponse
from photoVlogApp.models import Publicacion

def publicacionDetalle(request, id):
    publicacion = Publicacion.objects.get(pk =id)
    return HttpResponse(publicacion.titulo, publicacion.descripcion)

def publicaciones(request): 
    publicaciones = Publicacion.objects.order_by('id')

    return render(request , 'imagenes.html', {
            'publicaciones': publicaciones
         })
