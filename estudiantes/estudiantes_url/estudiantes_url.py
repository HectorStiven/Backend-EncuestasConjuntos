from django.urls import path
from estudiantes.viwesTotal import views

urlpatterns = [
    path('crear-t002datos-casa/', views.CrearT002DatosCasaVista.as_view(), name='crear_t002datos_casa'),
    path('listar-t002datos-casa/', views.ListarT002DatosCasaVista.as_view(), name='listar_t002datos_casa'),
    path('borrar-t002datos-casa/<int:pk>/', views.BorrarT002DatosCasaVista.as_view(), name='borrar_t002datos_casa'),
    path('actualizar-t002datos-casa/<int:pk>/', views.ActualizarT002DatosCasaVista.as_view(), name='actualizar_t002datos_casa'),

    # URLs para T007TiposDeCasa
    path('crear-t007tipos-de-casa/', views.CrearT007TiposDeCasaVista.as_view(), name='crear_t007tipos_de_casa'),
    path('listar-t007tipos-de-casa/', views.ListarT007TiposDeCasaVista.as_view(), name='listar_t007tipos_de_casa'),
    path('borrar-t007tipos-de-casa/<int:pk>/', views.BorrarT007TiposDeCasaVista.as_view(), name='borrar_t007tipos_de_casa'),
    path('actualizar-t007tipos-de-casa/<int:pk>/', views.ActualizarT007TiposDeCasaVista.as_view(), name='actualizar_t007tipos_de_casa'),

    # URLs para T003DatosConjunto
    path('crear-t003datos-conjunto/', views.CrearT003DatosConjuntoVista.as_view(), name='crear_t003datos_conjunto'),
    path('listar-t003datos-conjunto/', views.ListarT003DatosConjuntoVista.as_view(), name='listar_t003datos_conjunto'),
    path('borrar-t003datos-conjunto/<int:pk>/', views.BorrarT003DatosConjuntoVista.as_view(), name='borrar_t003datos_conjunto'),
    path('actualizar-t003datos-conjunto/<int:pk>/', views.ActualizarT003DatosConjuntoVista.as_view(), name='actualizar_t003datos_conjunto'),



# URLs para T004Personas
    path('crear-t004personas/', views.CrearT004PersonasVista.as_view(), name='crear_t004personas'),
    path('listar-t004personas/', views.ListarT004PersonasVista.as_view(), name='listar_t004personas'),
    path('borrar-t004personas/<int:pk>/', views.BorrarT004PersonasVista.as_view(), name='borrar_t004personas'),
    path('actualizar-t004personas/<int:pk>/', views.ActualizarT004PersonasVista.as_view(), name='actualizar_t004personas'),


     # Vistas para T005TipoAsistencia
    path('crear-t005tipo-asistencia/', views.CrearT005TipoAsistenciaVista.as_view(), name='crear_t005tipo_asistencia'),
    path('listar-t005tipo-asistencia/', views.ListarT005TipoAsistenciaVista.as_view(), name='listar_t005tipo_asistencia'),
    path('borrar-t005tipo-asistencia/<int:pk>/', views.BorrarT005TipoAsistenciaVista.as_view(), name='borrar_t005tipo_asistencia'),
    path('actualizar-t005tipo-asistencia/<int:pk>/', views.ActualizarT005TipoAsistenciaVista.as_view(), name='actualizar_t005tipo_asistencia'),



    path('crear-t006tipo-encuesta/', views.CrearT006TipoEncuestaVista.as_view(), name='crear_t006tipo_encuesta'),
    path('listar-t006tipo-encuesta/', views.ListarT006TipoEncuestaVista.as_view(), name='listar_t006tipo_encuesta'),
    path('borrar-t006tipo-encuesta/<int:pk>/', views.BorrarT006TipoEncuestaVista.as_view(), name='borrar_t006tipo_encuesta'),
    path('actualizar-t006tipo-encuesta/<int:pk>/', views.ActualizarT006TipoEncuestaVista.as_view(), name='actualizar_t006tipo_encuesta'),


    path('crear-t001encuesta/', views.CrearT001EncuestaVista.as_view(), name='crear_t001encuesta'),
    path('listar-t001encuesta/',views.ListarT001EncuestaVista.as_view(), name='listar_t001encuesta'),
    path('borrar-t001encuesta/<int:pk>/', views.BorrarT001EncuestaVista.as_view(), name='borrar_t001encuesta'),
    path('actualizar-t001encuesta/<int:pk>/', views.ActualizarT001EncuestaVista.as_view(), name='actualizar_t001encuesta'),

]

