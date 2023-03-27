from django.db import models

from departamentos.models import Departamento
# Create your models here.

class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    ci = models.CharField(max_length=50, unique=True)
    telefono = models.CharField(max_length=50)
    domicilio = models.CharField(max_length=50)
    sueldo = models.CharField(max_length=50)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    fecha_creacion = models.DateField(auto_now=True)

    class Meta:
        db_table = "Empleado"


    def __str__(self) -> str:
        return f"<{self.nombre} {self.apellido}>"