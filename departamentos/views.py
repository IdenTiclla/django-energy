from django.shortcuts import render, redirect

from django.contrib import messages

from departamentos.models import Departamento
# Create your views here.

def departamentos(request):
    if request.method == "GET":
        departamentos = Departamento.objects.all()
        return render(request, "departamentos/departamentos.html", {
            'departamentos': departamentos
        })
    
    elif request.method == "POST":
        print(request.POST)
        nombre = request.POST['nombre']
        ubicacion = request.POST['ubicacion']

        departamento = Departamento.objects.filter(nombre=nombre)
        if departamento:
            messages.add_message(request=request, level=messages.SUCCESS, message="Departamento ya existe")    
            return redirect('/departamentos')
        else:
            departamento = Departamento(nombre=nombre, ubicacion=ubicacion)
            departamento.save()
            messages.add_message(request=request, level=messages.SUCCESS, message="Departamento agregado correctamente!")
            return redirect('/departamentos')
        

def actualizar_departamento(request, id_departamento):
    departamento = Departamento.objects.get(id=id_departamento)
    if request.method == "GET":
        return render(request, "departamentos/actualizar_departamento.html", {
            'departamento': departamento
        })
    
    elif request.method == "POST":

        nombre = request.POST['nombre']
        ubicacion = request.POST['ubicacion']

        departamento.nombre = nombre
        departamento.ubicacion = ubicacion

        departamento.save()
        messages.add_message(request=request, level=messages.SUCCESS, message="Departamento Actualizado exitosamente!")
        return redirect('/departamentos')


def eliminar_departamento(request, id_departamento):
    departamento = Departamento.objects.get(id=id_departamento)
    departamento.delete()

    messages.add_message(request=request, level=messages.SUCCESS, message="Departamento Eliminado exitosamente!")

    return redirect("/departamentos")