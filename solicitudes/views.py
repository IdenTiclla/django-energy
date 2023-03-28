from django.shortcuts import render, redirect


from django.contrib import messages

from empleados.models import Empleado
from tecnicos.models import Tecnico
from solicitudes.models import Solicitud
# Create your views here.

def realizar_solicitud(request):
    if request.method == "GET":

        empleados = Empleado.objects.all()    
        tecnicos = Tecnico.objects.all()
        solicitudes = Solicitud.objects.all()   

        return render(request, "solicitudes/realizar_solicitud.html", {
            'empleados': empleados,
            'tecnicos': tecnicos,
            'solicitudes': solicitudes
        })
    elif request.method == "POST":
        print(request.POST)
        empleado_id = request.POST['empleado_id']
        tecnico_id = request.POST['tecnico_id']
        
        empleado = Empleado.objects.get(id=empleado_id)
        tecnico = Tecnico.objects.get(id=tecnico_id)

        nombre_equipo = request.POST['nombre_equipo']
        
        problema = request.POST['problema']

        descripcion = request.POST['descripcion']
        print(empleado_id)
        print(tecnico_id)
        print(descripcion)

        solicitud = Solicitud(empleado=empleado, tecnico=tecnico, nombre_equipo=nombre_equipo, problema=problema, descripcion=descripcion)

        solicitud.save()

        messages.add_message(request=request, level=messages.SUCCESS, message="Solicitud de reparacion realizada correctamente!")

        return redirect('/realizar_solicitud')
    

def solicitudes_realizadas(request):
    solicitudes = Solicitud.objects.filter(estado="Solicitado")
    return render(request, "solicitudes/sistemas_solicitudes_realizadas.html", {
        'solicitudes': solicitudes
    })


def ver_solicitud(request, solicitud_id):
    solicitud = Solicitud.objects.get(id=solicitud_id)
    print(solicitud_id)
    print(solicitud)
    return render(request, "solicitudes/ver_solicitud.html", {
        'solicitud': solicitud
    })