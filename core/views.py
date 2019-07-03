from django.shortcuts import render
<<<<<<< HEAD
from.forms import estudioFormu,pacienteFormu
=======
from.forms import estudioFormu
>>>>>>> 7927276fd1b2c4dd6dc819fd275d3e6d654cb1e2
# Create your views here
#en esta parte se generan las vistas para direccionar nuestra app 
def fomPaciente(request):
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

<<<<<<< HEAD
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
    



=======
>>>>>>> 7927276fd1b2c4dd6dc819fd275d3e6d654cb1e2

