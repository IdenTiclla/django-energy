from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index),
    path('empleados', views.empleados),

    path("empleados/update/<int:id_empleado>", views.actualizar_empleado),
    path("empleados/delete/<int:id_empleado>", views.eliminar_empleado)

]
