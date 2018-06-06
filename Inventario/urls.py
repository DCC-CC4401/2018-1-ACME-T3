from django.urls import path
from . import views

app_name = 'Inventario'

urlpatterns = [
    path('', views.index, name='index'),
    path('perfil/', views.perfilUsuario, name='perfilUsuario'),
    path('articulo/<int:articuloId>/', views.fichaArticulo, name='fichaArticulo'),
    path('lpadmin/', views.landingPageAdministrador, name='lpAdmin'),
    path('lpusuario/', views.landingPageUsuario, name='lpUsuario'),
    path('buscar/', views.busquedaArticulos, name='buscar'),
    path('buscar/articulo/<int:articuloId>/', views.fichaArticulo, name='articuloEncontrado')
]
