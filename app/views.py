from django.contrib import messages
from django.shortcuts import redirect, render
import bcrypt
from .decorators import login_required
from .models import *


@login_required
def index(request):
    context = {
        'mensajes': Mensaje.objects.all(),
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
        #return redirect("/Shows/New")
        return redirect("/")
    else:
        mensaje_creado = request.POST['mensaje']
        user_id_creador = request.POST['id_user_post']

        mensaje = Mensaje.objects.create(
            mensaje = mensaje_creado, 
            user = User.objects.get(id=user_id_creador),
        )
        messages.success(request, "Mensaje agregado correctamente")

        #return redirect(f"/Shows/{show.id}")
        return redirect(f"/")