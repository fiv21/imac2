from django.shortcuts import render
from.forms import estudioFormu,pacienteFormu
from.models import Pacientes
from django.views.generic import ListView
# Create your views here
#en esta parte se generan las vistas para direccionar nuestra app 
def fomPaciente(request):
    if request.method == 'GET':
        q = request.GET.get('q', '')
        eventos = Pacientes.objects.filter(nombre__icontains=q)
        return render(request, 'core/formPaciente.html', {'eventos': eventos})

    if request.method == 'POST':
        form=estudioFormu(request.POST) #indico metodos POST de la transmicion de mis datos
        if form.is_valid(): #pregunto si mis datos son validos
            form.save() #guardo
        return render(request,"core/home.html")#al ser esto exitoso redirecciono a home
    else:
        form=estudioFormu()#caso contrario atualizo la misma pagina del forulario
    return render(request,"core/formPaciente.html",{'form':form}) #renerizo indicando que exitste formulario
#funcion pagina home Home.
def home(request):
    return render(request,"core/home.html",context=None) #funcion de la vista home 

#carga del formulario de los pacientes.

def cargaPacientes(request):
    if request.method == 'POST':
        form=pacienteFormu(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return render(request,"core/home.html")
    else:
        form=pacienteFormu
    return render (request,"core/cargapaciente.html",{'form':form})

class Listapacientes(ListView):
    model = Pacientes
    template_name = 'core/listapacientes.html'




