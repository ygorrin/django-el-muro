from django.contrib import messages
from django.shortcuts import redirect, render
import bcrypt
from .decorators import login_required
from .models import *


@login_required
def index(request):
    #id_user = request.POST['id_user']
    context = {
        'mensajes': Mensaje.objects.all(),
        'comentarios': Comentario.objects.all(),
        #'user' : User.objects.get(id = id_user),
    }
    return render(request, 'index.html', context)

@login_required
def mensaje_crear(request):
    print(request.POST)

    errors= Mensaje.objects.validador_basico_mensaje(request.POST)
    print(errors)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        mensaje_creado = request.POST['mensaje']
        #user_id_creador = request.POST['id_user_post']
        #print("ID del ususario", user_id_creador)
        user_id_creador = request.session['usuario']['id']
        #user_id_creador = usuario.id

        mensaje = Mensaje.objects.create(
            mensaje = mensaje_creado, 
            user = User.objects.get(id = user_id_creador),
        )
        messages.success(request, "Mensaje agregado correctamente")

        return redirect(f"/")



@login_required
def comentario_crear(request):
    print(request.POST)

    errors= Comentario.objects.validador_basico_comentario(request.POST)
    print(errors)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        comentario_creado = request.POST['comentario']
        id_mensaje = request.POST['id_mensaje_comentario']
        #comentario_user_id = request.POST['id_user_comentario']
        comentario_user_id = request.session['usuario']['id']

        comentario = Comentario.objects.create(
            comentario = comentario_creado, 
            user = User.objects.get(id=comentario_user_id),
            mensaje = Mensaje.objects.get(id=id_mensaje),
        )
        messages.success(request, "Comentario agregado correctamente")

        return redirect(f"/")