from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Esta es mi web.")

def otravista(request):
    return HttpResponse("Esta es otra vista de mi web.")

def suma(request, numero1, numero2):
    resultado = numero1 + numero2
    return HttpResponse(resultado)
    
def calculadora(request, operacion, numero1, numero2):
    

    if operacion == 'suma':
        return suma(request, numero1, numero2)
    else:
        return HttpResponse('no entendí')