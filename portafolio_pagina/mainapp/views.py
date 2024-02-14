from django.shortcuts import render
from mainapp.models import ImageOfTheDay
import requests
from datetime import datetime
import json
import webbrowser


def index(request):
    FechaActualizada = comprobarFechaAPOD(request)

    if not FechaActualizada:
        print("actualizando registros")
        nasaAPOD(request)
    else:
        print("no fue necesario actualizar registro")

    ultimoRegistro = ImageOfTheDay.objects.latest("last_updated")
    imagen_del_diaURL = ultimoRegistro.image_url
    print(f"{imagen_del_diaURL} url a mandar a index")

    return render(request, 'mainapp/index.html', {
        'title': 'inicio',
        'imageOfTheDay' : imagen_del_diaURL
    })


def about(request):
    return render(request, 'mainapp/about.html', {
        'title': 'sobre nosotros'
    })

def contacto(request):
    return render(request, 'mainapp/contacto.html')


def experiencia(request):
    return render(request, 'mainapp/experiencia.html')

def comprobarFechaAPOD(request):
    fecha_de_hoy = datetime.now().date()
    ultimo_registro = ImageOfTheDay.objects.latest("last_updated")
    fecha_ultimo_registro = ultimo_registro.last_updated
    print(fecha_ultimo_registro)
    print(fecha_de_hoy)

    if fecha_de_hoy == fecha_ultimo_registro:
        return True
    else :
        return False

def nasaAPOD(request):
    fecha_hoy = datetime.now().date()
    API_KEY = 'zMm2wEorcFjh2W3pbUnPMQwEbMb1PYxD6CdQTKpu'
    url = 'https://api.nasa.gov/planetary/apod'

    params = {
        'api_key': API_KEY,
        'hd': 'False',
        'date': fecha_hoy
    }

    response = requests.get(url, params=params)
    json_data = json.loads(response.text)
    image_url = json_data['url']

    # Crear una nueva instancia de ImageOfTheDay y guardarla en la base de datos
    nueva_imagen = ImageOfTheDay.objects.create(image_url=image_url, last_updated=datetime.now().date())

    print(image_url)

    return nueva_imagen

    
# Create your views here.
