from django.db import models

# Create your models here.


class Departamento(models.Model):
    nombre = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=50)

    fecha_creacion = models.DateField(auto_now=True)


    class Meta:
        db_table = "Departamento"

    def __str__(self) -> str:
        return f"<{self.nombre}"