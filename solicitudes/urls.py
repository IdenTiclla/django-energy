from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index),
    # gestion repuestos

    path('repuestos', views.repuestos),
    path("repuestos/update/<int:repuesto_id>", views.actualizar_repuesto),
    path("repuestos/delete/<int:repuesto_id>", views.eliminar_repuesto),


    # solicitudes
    path('realizar_solicitud', views.realizar_solicitud),

    path('solicitudes_realizadas', views.solicitudes_realizadas),

    path('ver/solicitud/<int:solicitud_id>', views.ver_solicitud),


    path('solicitudes_en_progreso', views.solicitudes_en_progreso),


    # para soporte cambiar los estados

    path("poner_solicitud_en_progreso/solicitud/<int:solicitud_id>", views.poner_solicitud_en_progreso),
    
    # agregar solucion a solicitud
    path("agregar_solucion/solicitud/<int:solicitud_id>", views.agregar_solucion),


    

    #path("solicitudes/update/<int:id_solicitud>", views.actualizar_solicitud),
    #path("solicitudes/delete/<int:id_solicitud>", views.eliminar_solicitud)

]
