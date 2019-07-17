from django.shortcuts import render
from.forms import FormularioErgometria
from core.models import Pacientes
# Create your views here.

def cargaErgo(request):
    if request.method == 'GET':
        q = request.GET.get('q', '')
        eventos = Pacientes.objects.filter(nombre__icontains=q)
        return render(request, 'ergo/ergometria.html', {'eventos': eventos})
    if request.method == 'POST':
        form=FormularioErgometria(request.POST) #indico metodos POST de la transmicion de mis datos
        if form.is_valid():
             #pregunto si mis datos son validos
            form.save(commit=True) #guardo
        return render(request,"core/home.html")#al ser esto exitoso redirecciono a home
    else:
        form=FormularioErgometria()#caso contrario atualizo la misma pagina del forulario
        return render(request,'ergo/ergometria.html')#renerizo indicando que exitste formulario
    return render(request,"'ergo/ergometria.html",{'form':form})