from django.shortcuts import render, redirect


from django.contrib import messages

from empleados.models import Empleado
from tecnicos.models import Tecnico
from solicitudes.models import Solicitud, Repuesto, Solucion, SolucionRepuesto
# Create your views here.

# repuestos

def repuestos(request):
    if request.method == "GET":
        repuestos = Repuesto.objects.all()
        return render(request, "repuestos/repuestos.html", {
            'repuestos': repuestos,
        })
    
    elif request.method == "POST":
        print(request.POST)
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']

        repuesto = Repuesto.objects.filter(nombre=nombre)
        if repuesto:
            messages.add_message(request=request, level=messages.SUCCESS, message="Repuesto ya existe")    
            return redirect('/repuestos')
        else:
            repuesto = Repuesto(nombre=nombre, descripcion=descripcion)
            repuesto.save()
            messages.add_message(request=request, level=messages.SUCCESS, message="Repuesto agregado correctamente!")
            return redirect('/repuestos')
        

def actualizar_repuesto(request, repuesto_id):
    repuesto = Repuesto.objects.get(id=repuesto_id)

    if request.method == "GET":
        return render(request, "repuestos/actualizar_repuesto.html", {
            'repuesto': repuesto,
        })
    
    elif request.method == "POST":

        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        

        repuesto.nombre = nombre
        repuesto.descripcion = descripcion


        repuesto.save()
        messages.add_message(request=request, level=messages.SUCCESS, message="Repuesto Actualizado exitosamente!")
        return redirect('/repuestos')


def eliminar_repuesto(request, repuesto_id):
    repuesto = Repuesto.objects.get(id=repuesto_id)
    repuesto.delete()

    messages.add_message(request=request, level=messages.SUCCESS, message="Repuesto Eliminado exitosamente!")

    return redirect("/repuestos")

# solicitudes
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

def solicitudes_en_progreso(request):
    solicitudes = Solicitud.objects.filter(estado="En progreso")
    return render(request, "solicitudes/sistemas_solicitudes_en_progreso.html", {
        'solicitudes': solicitudes
    })

def solicitudes_pendiente_aprobacion(request):
    solicitudes = Solicitud.objects.filter(estado="Pendiente aprobacion")
    return render(request, "solicitudes/sistemas_solicitudes_pendientes_de_aprobacion.html", {
        'solicitudes': solicitudes
    })

def solicitudes_aprobadas(request):
    solicitudes = Solicitud.objects.filter(estado='Aprobada')
    return render(request, "solicitudes/sistemas_solicitudes_aprobadas.html", {
        'solicitudes': solicitudes
    })


def poner_solicitud_en_progreso(request, solicitud_id):
    solicitud = Solicitud.objects.get(id=solicitud_id)
    print(solicitud_id)
    print(solicitud)
    # cambiando el estado a En progreso
    solicitud.estado = "En progreso"
    solicitud.save()
    messages.add_message(request=request, level=messages.SUCCESS, message="Solicitud puesta en  progreso!")
    return redirect('/solicitudes_en_progreso')


def agregar_solucion(request, solicitud_id):
    solicitud = Solicitud.objects.get(id=solicitud_id)
    repuestos = Repuesto.objects.all()
    if request.method == "GET":
        print(solicitud_id)
        print(solicitud)
        return render(request, "solicitudes/agregar_solucion_solicitud.html", {
            'solicitud': solicitud,
            'repuestos': repuestos
        })
    elif request.method == "POST":
        print(request.POST)
        fallas_reales = request.POST['fallas_reales']
        solucion_realizada = request.POST['solucion_realizada']
        solucion = Solucion(fallas_reales=fallas_reales, solucion_realizada=solucion_realizada)
        solucion.save()
        
        solicitud.solucion = solucion
        solicitud.save()
        # si nos pasaron los repuestos entonces debemos guardarlos
        if 'repuestos_id' in request.POST:
            print("se pasaron los repuestos") 
            repuestos_id = request.POST['repuestos_id']
            for repuesto_id in repuestos_id:
                print(repuesto_id)
                repuesto = Repuesto.objects.get(id=repuesto_id)
                solucion_repuesto = SolucionRepuesto(solucion=solucion, repuesto=repuesto)
                solucion_repuesto.save()

        solicitud.estado = "Pendiente aprobacion"
        solicitud.save()

        messages.add_message(request=request, level=messages.SUCCESS, message="Solucion agregada solicitud pendiente de aprobacion!")
        return redirect('/solicitudes_aprobadas')
    

def aprobar_solicitud(request, solicitud_id):
    print(solicitud_id)
    solicitud = Solicitud.objects.get(id=solicitud_id)
    
    # cambiando el estado a En progreso
    solicitud.estado = "Aprobada"
    solicitud.save()
    messages.add_message(request=request, level=messages.SUCCESS, message="Solicitud aprobada!")
    return redirect('/solicitudes_aprobadas')