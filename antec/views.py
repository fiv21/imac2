from django.shortcuts import render
<<<<<<< HEAD
from.forms import formAntecedentes
from core.models import Pacientes 
# Create your views here.

def form_antecedente(request):
    antecedente = Pacientes.objects.all()
    context = {'antec':antecedente}
    if request.method == 'POST':
        form=formAntecedentes(request.POST) #indico metodos POST de la transmicion de mis datos
        if form.is_valid():
             #pregunto si mis datos son validos
            form.save(commit=True) #guardo
        return render(request,"core/home.html")#al ser esto exitoso redirecciono a home
    else:
        form=formAntecedentes#caso contrario atualizo la misma pagina del forulario
    return render(request,"antec/antecedentes.html",{'form':form},context) #renerizo indicando que exitste formulario


=======

# Create your views here.
>>>>>>> 7927276fd1b2c4dd6dc819fd275d3e6d654cb1e2
