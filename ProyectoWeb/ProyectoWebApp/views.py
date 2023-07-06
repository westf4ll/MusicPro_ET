from django.conf import settings
from django.templatetags.static import static
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader 
from datetime import datetime as dt
from datetime import timedelta
import random
import requests

from transbank.error.transbank_error import TransbankError
from transbank.webpay.webpay_plus.transaction import Transaction

# Create your views here.

def home(request):

    return render(request, "ProyectoWebApp/home.html")

def servicios(request):
    return render(request, "ProyectoWebApp/servicios.html")


def blog(request):   
    return render(request, "ProyectoWebApp/blog.html")



def tienda(request):
    url = "https://api.reverb.com/api/listings"
    headers = {
        "Authorization": "Bearer e45ab2c1dce0177f23c85c17dba97dc54767c84e6337957a8779ad1f24885d79",
        "Content-Type": "application/json",
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        instrumentos = data.get("listings", [])

        for instrumento in instrumentos:
            photos = instrumento.get("photos", [])
            if photos:
                instrumento["image_url"] = photos[0]["_links"]["large_crop"]["href"]
            else:
                instrumento["image_url"] = None

        context = {"instrumentos": instrumentos}
    else:
        context = {
            "error_message": "No se pudieron cargar los productos. Por favor, inténtalo de nuevo más tarde."
        }

    return render(request, "ProyectoWebApp/tienda.html", context)
    

def aprobado(request):
    return render(request, "ProyectoWebApp/aprobado.html")

def error(request):
    return render(request, "ProyectoWebApp/error.html")


def contact(request):
    return render(request, "ProyectoWebApp/contact.html")






#transbank
def pago(request):

    buy_order = str(random.randrange(1000000, 99999999))
    session_id = str(random.randrange(1000000, 99999999))
    amount = random.randrange(10000, 1000000)
    return_url = "http://127.0.0.1:8000/aprobado"

    create_request = {
        "buy_order": buy_order,
        "session_id": session_id,
        "amount": amount,
        "return_url": return_url
    }

    response = (Transaction()).create(
        buy_order, session_id, amount, return_url)

    contexto = {
        "instancia": response
    }

    #4051 8842 3993 7763

    return render(request, "ProyectoWebApp/pago.html", contexto)

#api de instrumentos



