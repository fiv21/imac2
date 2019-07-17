from django.urls import path
from django.contrib.auth.views import LoginView 
from django.contrib.auth import views as auth_views
from core.views import Listapacientes,home,fomPaciente,cargaPacientes 
#aca genero las urls que va a tener la app core de nuestro proyecto 
urlpatterns = [

    #path del core
    path('principal/', home, name="home"),
    path('formpaciente/', fomPaciente, name="form"),
    path('cargapaciente/', cargaPacientes, name="pacienteform"),
    path('listapacientes/', Listapacientes.as_view(), name='pacienteslistado'),
    path('', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
]