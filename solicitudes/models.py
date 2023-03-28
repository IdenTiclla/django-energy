from django.db import models

from empleados.models import Empleado
from tecnicos.models import Tecnico
# Create your models here.



class Solucion(models.Model):
    fallas_reales = models.CharField(max_length=255)
    solucion_realizada = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return f"<{self.nombre}>"
    
    class Meta:
        db_table = "Solucion"


class Repuesto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"<{self.nombre}>"
    
    class Meta:
        db_table = "Repuesto"


class SolucionRepuesto(models.Model):
    solucion = models.ForeignKey(Solucion, on_delete=models.CASCADE)
    repuesto = models.ForeignKey(Repuesto, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"<{self.solucion.fallas_reales} - {self.repuesto.nombre}>"


    class Meta:
        db_table = "SolucionRepuesto"


class Solicitud(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE)
    nombre_equipo = models.CharField(max_length=50)

    problema = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255)
    fecha_creacion = models.DateField(auto_now=True)
    estado = models.CharField(max_length=20, default="Solicitado")
    # debemos aceptar valores nulos para luego darle una solucion
    solucion = models.ForeignKey(Solucion, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self) -> str:
        return f"<{self.nombre_equipo} - {self.empleado.nombre} {self.tecnico.nombre}>"
    
    class Meta:
        db_table = "Solicitud"