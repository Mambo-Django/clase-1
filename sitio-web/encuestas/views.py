from django.http import HttpResponse
from django.shortcuts import render, redirect

from encuestas.models import Usuario

from services.register import RegisterModule

import datetime as dt


# usuarios = [ {'name': 'hernan', 'password':'Wilkinson'}, 
#              { 'name': 'fabio', 'password': 'Tobis'} ]

# Create your views here.
def index(request):
    return HttpResponse("Esta es mi web.")

def login(request):
    return render(request, 'encuestas/formulario.html')

def registrate(request):
    # var = RegisterModule.prueba()
    # print(var)
    if request.method == 'POST':
        ## Acá nos aseguramos que se procesó el formulario.
        usuario_post = request.POST.get('usuario') # Nombre de usuario
        usuario_existe = Usuario.objects.filter(usuario=usuario_post)
        
        if not usuario_existe:
            # No grabar porque ya está registrado
            nombre = request.POST.get('nombre')
            password_post = request.POST.get('password')
            edad = request.POST.get('edad')
            fecha_actual = dt.datetime.now()
            ## HAY QUE REGISTRARLO. 
            usuario = Usuario.objects.create(nombre=nombre, usuario=usuario_post, password=password_post, edad=edad, edad_padre=edad, fecha_registro=fecha_actual)
            usuario.save()
        
        return render(request, 'encuestas/formulario.html')

    else:
        return render(request, 'encuestas/formulario_registro.html')

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

