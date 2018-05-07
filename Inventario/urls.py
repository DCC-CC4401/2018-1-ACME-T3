from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('usuario/<int:userId>/', views.perfilUsuario, name='perfilUsuario'),
    path('administrador/', views.landingPageAdministrador, name='perfilAdmin')
]