from django.shortcuts import render, redirect

from django.contrib import messages

from tecnicos.models import Tecnico
# Create your views here.


def tecnicos(request):
    if request.method == "GET":
        tecnicos = Tecnico.objects.all()
        return render(request, "tecnicos/tecnicos.html", {
            'tecnicos': tecnicos,
        })
    
    elif request.method == "POST":
        print(request.POST)
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        ci = request.POST['ci']
        telefono = request.POST['telefono']
        domicilio = request.POST['domicilio']


        tecnico = Tecnico.objects.filter(nombre=nombre, apellido=apellido, ci=ci)
        if tecnico:
            messages.add_message(request=request, level=messages.SUCCESS, message="Tecnico ya existe")    
            return redirect('/tecnicos')
        else:
            tecnico = Tecnico(nombre=nombre, apellido=apellido, ci=ci, telefono=telefono, domicilio=domicilio)
            tecnico.save()
            messages.add_message(request=request, level=messages.SUCCESS, message="Tecnico agregado correctamente!")
            return redirect('/tecnicos')
        

def actualizar_tecnico(request, tecnico_id):
    tecnico = Tecnico.objects.get(id=tecnico_id)

    if request.method == "GET":
        return render(request, "tecnicos/actualizar_tecnico.html", {
            'tecnico': tecnico,
        })
    
    elif request.method == "POST":

        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        ci = request.POST['ci']
        telefono = request.POST['telefono']
        domicilio = request.POST['domicilio']
        

        tecnico.nombre = nombre
        tecnico.apellido = apellido
        tecnico.ci = ci
        tecnico.telefono = telefono
        tecnico.domicilio = domicilio


        tecnico.save()
        messages.add_message(request=request, level=messages.SUCCESS, message="Tecnico Actualizado exitosamente!")
        return redirect('/tecnicos')


def eliminar_tecnico(request, tecnico_id):
    tecnico = Tecnico.objects.get(id=tecnico_id)
    tecnico.delete()

    messages.add_message(request=request, level=messages.SUCCESS, message="Tecnico Eliminado exitosamente!")

    return redirect("/tecnicos")