from django.shortcuts import render
<<<<<<< HEAD
from.forms import FormErgometria
# Create your views here.

def cargaErgo(request):
    if request.method == 'POST':
        form=FormErgometria(request.POST) #indico metodos POST de la transmicion de mis datos
        if form.is_valid(): #pregunto si mis datos son validos
            form.save(commit=True) #guardo
        return render(request,"core/home.html")#al ser esto exitoso redirecciono a home
    else:
        form=FormErgometria#caso contrario atualizo la misma pagina del forulario
    return render(request,"ergo/ergometria.html",{'form':form})
=======

# Create your views here.
>>>>>>> 7927276fd1b2c4dd6dc819fd275d3e6d654cb1e2
