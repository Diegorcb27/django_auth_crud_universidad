from django.urls import path
from .views import home, registrarCurso, eliminarCurso, edicionCurso, editarCurso

app_name='academico_urls'





urlpatterns=[
      path('', home, name="home" ),
      path('registrarCurso/', registrarCurso, name="registrarCurso"),
      path('edicionCurso/<codigo>', edicionCurso, name="edicionCurso" ),
      path('editarCurso/', editarCurso, name="editarCurso"),
      path('eliminacionCurso/<codigo>', eliminarCurso, name="eliminarCurso")
]