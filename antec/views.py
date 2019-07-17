from django.shortcuts import render
from.forms import formAntecedentes
from django.db.models import Q
from core.models import Pacientes 
# Create your views here.

def form_antecedente(request):



#agregando busqueda 
   # if request.method == 'POST':
      #  srch=request.POST['srh']
       # if srch:
         #   match=Pacientes.objects.filter(Q(nombre__icontains=srch)  |  Q(dni__icontains=srch))
          #  if match:
           #     return render(request,"antec/antecedentes.html",{'sr':match})
            #else:
             #   return render(request,'core/home.html')
    #return render(request,'antec/antecedentes.html')

    #####agregando prueba busqueda.
    if request.method == 'GET':
        q = request.GET.get('q', '')
        eventos = Pacientes.objects.filter(nombre__icontains=q)
        return render(request, 'antec/antecedentes.html', {'eventos': eventos})


    if request.method == 'POST':
        form=formAntecedentes(request.POST) #indico metodos POST de la transmicion de mis datos
        if form.is_valid():
             #pregunto si mis datos son validos
            form.save(commit=True) #guardo
        return render(request,"core/home.html")#al ser esto exitoso redirecciono a home
    else:
        form=formAntecedentes#caso contrario atualizo la misma pagina del forulario
        return render(request,'antec/antecedentes.html')#renerizo indicando que exitste formulario
    return render(request,"antec/antecedentes.html",{'form':form})
