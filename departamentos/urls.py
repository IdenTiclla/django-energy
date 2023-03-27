from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index),
    path('departamentos', views.departamentos),

    path("departamentos/update/<int:id_departamento>", views.actualizar_departamento),
    path("departamentos/delete/<int:id_departamento>", views.eliminar_departamento)

]
