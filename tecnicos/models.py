from django.db import models

# Create your models here.

class Tecnico(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    ci = models.CharField(max_length=50, unique=True)
    telefono = models.CharField(max_length=50)
    domicilio = models.CharField(max_length=50)

    fecha_creacion = models.DateField(auto_now=True)

    class Meta:
        db_table = "Tecnico"


    def __str__(self) -> str:
        return f"<{self.nombre} {self.apellido}>"