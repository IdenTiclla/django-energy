from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, redirect

from django.contrib import messages

from empleados.models import Empleado
from departamentos.models import Departamento
# Create your views here.

def empleados(request):
    if request.method == "GET":
        empleados = Empleado.objects.all()
        departamentos = Departamento.objects.all()
        return render(request, "empleados/empleados.html", {
            'empleados': empleados,
            'departamentos': departamentos
        })
    
    elif request.method == "POST":
        print(request.POST)
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        ci = request.POST['ci']
        telefono = request.POST['telefono']
        domicilio = request.POST['domicilio']
        sueldo = request.POST['sueldo']

        departamento_id = request.POST['departamento_id']
        departamento = Departamento.objects.get(id=departamento_id)

        empleado = Empleado.objects.filter(nombre=nombre, apellido=apellido, ci=ci)
        if empleado:
            messages.add_message(request=request, level=messages.SUCCESS, message="Empleado ya existe")    
            return redirect('/empleados')
        else:
            empleado = Empleado(nombre=nombre, apellido=apellido, ci=ci, telefono=telefono, domicilio=domicilio, sueldo=sueldo, departamento=departamento)
            empleado.save()
            messages.add_message(request=request, level=messages.SUCCESS, message="Empleado agregado correctamente!")
            return redirect('/empleados')
        

def actualizar_empleado(request, id_empleado):
    empleado = Empleado.objects.get(id=id_empleado)
    departamentos = Departamento.objects.all()

    if request.method == "GET":
        return render(request, "empleados/actualizar_empleado.html", {
            'empleado': empleado,
            'departamentos': departamentos
        })
    
    elif request.method == "POST":

        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        ci = request.POST['ci']
        telefono = request.POST['telefono']
        domicilio = request.POST['domicilio']
        sueldo = request.POST['sueldo']
        
        departamento_id = request.POST['departamento_id']
        departamento = Departamento.objects.get(id=departamento_id)

        empleado.nombre = nombre
        empleado.apellido = apellido
        empleado.ci = ci
        empleado.telefono = telefono
        empleado.domicilio = domicilio
        empleado.sueldo = sueldo

        empleado.departamento = departamento

        empleado.save()
        messages.add_message(request=request, level=messages.SUCCESS, message="Empleado Actualizado exitosamente!")
        return redirect('/empleados')


def eliminar_empleado(request, id_empleado):
    empleado = Empleado.objects.get(id=id_empleado)
    empleado.delete()

    messages.add_message(request=request, level=messages.SUCCESS, message="Empleado Eliminado exitosamente!")

    return redirect("/empleados")