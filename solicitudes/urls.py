from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index),
    path('realizar_solicitud', views.realizar_solicitud),

    path('solicitudes_realizadas', views.solicitudes_realizadas),

    

    #path("solicitudes/update/<int:id_solicitud>", views.actualizar_solicitud),
    #path("solicitudes/delete/<int:id_solicitud>", views.eliminar_solicitud)

]
