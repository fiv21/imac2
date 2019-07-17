from django.shortcuts import render
from.forms import ventricularFormu
from core.models import Pacientes
# Create your views here.

def formventricular(request):
    
    if request.method == 'GET':
        q = request.GET.get('q', '')
        eventos = Pacientes.objects.filter(nombre__icontains=q)
        return render(request, 'fventricular/fventricular.html', {'eventos': eventos})



    if request.method == 'POST':
        form=ventricularFormu(request.POST) #indico metodos POST de la transmicion de mis datos
        if form.is_valid(): #pregunto si mis datos son validos
            form.save() #guardo
        return render(request,"core/home.html")#al ser esto exitoso redirecciono a home
    else:
        form=ventricularFormu()#caso contrario atualizo la misma pagina del forulario
    return render(request,"fventricular/fventricular.html",{'form':form})