from django.http import HttpResponse
from django.shortcuts import render, redirect

usuarios = [ {'name': 'hernan', 'password':'Wilkinson'}, 
             { 'name': 'fabio', 'password': 'Tobis'} ]

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

def login(request):
    return render(request, 'encuestas/formulario.html')

# Acá vamos a crear una función que verifique los usuarios
def verificar(request):
    
    if request.method == 'POST':
        usuario_post = request.POST.get('usuario')
        password_post = request.POST.get('password')

        # --> insertamos la lógica de chequear
        # si el usuario es posta y si su contraseña coincide.
        for usuario in usuarios:
            # usuario -> { 'name': 'pepito', 'password':'pepito' }
            if usuario['name'] == usuario_post:
                if usuario['password'] == password_post:
                    return render(request, 'encuestas/home.html')
                else:
                    response = redirect('login', kwargs={'mensaje_error': 'Pusiste mal la contraseña.'})
                    return response
        
        return render(request, 'encuestas/formulario.html', {'error': 'No existis.'})

    else:
        return HttpResponse('Esto no es un método post.')

