from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('proyectos/', views.lista_proyectos, name='lista_proyectos'),
    path('proyectos/create/', views.crear_proyecto, name='crear_proyecto'),
    path('proyectos/<int:proyecto_id>/', views.detalle_proyecto, name='detalle_proyecto'),
    path('proyectos/<int:proyecto_id>/editar/', views.editar_proyecto, name='editar_proyecto'),
    path('proyectos/<int:proyecto_id>/eliminar/', views.eliminar_proyecto, name='eliminar_proyecto'),
    

    path('tareas/', views.listar_tareas, name='listar_tareas'),
    path('proyectos/<int:proyecto_id>/tareas/crear/', views.crear_tarea, name='crear_tarea'),

    path('proyectos/<int:proyecto_id>/tareas/crear/', views.crear_tarea, name='crear_tarea'),
    path('proyectos/<int:proyecto_id>/tareas/', views.lista_tareas, name='lista_tareas'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
