from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index),
    path('tecnicos', views.tecnicos),
    path("tecnicos/update/<int:tecnico_id>", views.actualizar_tecnico),
    path("tecnicos/delete/<int:tecnico_id>", views.eliminar_tecnico)

]
