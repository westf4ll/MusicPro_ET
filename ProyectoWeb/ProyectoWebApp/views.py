from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from django.template import loader 
from datetime import datetime as dt
from datetime import timedelta
import random

from transbank.error.transbank_error import TransbankError
from transbank.webpay.webpay_plus.transaction import Transaction

# Create your views here.

def home(request):

    return render(request, "ProyectoWebApp/home.html")

def servicios(request):
    
    return render(request, "ProyectoWebApp/servicios.html")

def blog(request):
    
    return render(request, "ProyectoWebApp/blog.html")

def contact(request):
    
    return render(request, "ProyectoWebApp/contact.html")

def tienda(request):
    
    return render(request, "ProyectoWebApp/tienda.html")

def pago(request):

    buy_order = str(random.randrange(1000000, 99999999))
    session_id = str(random.randrange(1000000, 99999999))
    amount = random.randrange(10000, 1000000)
    return_url = "http://127.0.0.1:8000/"

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

    return render(request, 'ProyectoWebApp/pago.html', contexto)
