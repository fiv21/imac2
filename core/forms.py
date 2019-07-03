from django import forms
<<<<<<< HEAD
from.models import Estudio, Pacientes
=======
from.models import Estudio,Pacientes

>>>>>>> 7927276fd1b2c4dd6dc819fd275d3e6d654cb1e2

#en esta parte se genera el back end de los formularios web 
#generando otra forma de cargar los datos desde la pagina web

class estudioFormu(forms.ModelForm):
    class Meta:
        model=Estudio # aca indicamos los campos que vamos a utilizar 

        fields= [
            'pacientes',         #se realizo cambio en el formulario con la relacion de la tabla paciente y estudio
            'instituciones',
            'medico',
            'peso',     
            'talla',
            'indicacion',
            'decubito',
            'perimetroAbdominal',
            'edad',
            'urgencia',
            'imc',
            'supCorporal',
            'calidadTecnica',
            'observaciones',
        ]
        labels = {
            
            'pacientes' :'Paciente',
            'instituciones' : 'Instituciones',
            'medico' : 'Medico',
            'peso' : 'Peso',
            'talla' : 'Talla',
            'indicacion' : 'Indicacion',
            'decubito' : 'Decubito',
            'perimetroAbdominal' : 'Perimetro abdominal',
            'edad': 'Edad',
            'urgencia':'Urgencia',
            'imc' : 'Imc',
            'supCorporal' : 'Superficie corporal',
            'calidadTecnica' : 'Calidad tecnica',
            'observaciones' : 'Observaciones',
        }

        widgets={
            'pacientes':forms.Select(attrs={'class':'form-control' ,'style':'height:30px' }),
            'instituciones':forms.Select(attrs={'class':'form-control','style':'height:30px'}),
            'medico':forms.TextInput(attrs={'class':'form-control'}),
            'peso':forms.TextInput(attrs={'class':'form-control'}),
            'indicacion':forms.TextInput(attrs={'class':'form-control'}),
            'decubito':forms.TextInput(attrs={'class':'form-control'}),
            'perimetroAbdominal':forms.TextInput(attrs={'class':'form-control'}),
            'edad':forms.TextInput(attrs={'class':'form-control'}),
            'imc':forms.TextInput(attrs={'class':'form-control'}),
            'supCorporal':forms.TextInput(attrs={'class':'form-control'}),
            'calidadTecnica':forms.TextInput(attrs={'class':'form-control'}),
            'observaciones':forms.Textarea(attrs={'class':'form-control'}),
            
        }

#crear Formulario de los pacientes.
<<<<<<< HEAD

class pacienteFormu(forms.ModelForm):
    class Meta:
        model=Pacientes

        fields=[
            'nombre',
            'apellido',
            'dni',
            'nacionalidad',
            'domicilio',
            'numero_domicilio',
            'cobertura_medica',
            'numero_afilido',
            'sexo',
            'fecha_nacimiento',

        ]

        labels={
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'dni':'Dni',
            'nacionalidad':'Nacionalidad',
            'domicilio':'Domicilio',
            'numero_domicilio':'Numero de domicilio',
            'cobertura_medica':'Cobertura medica',
            'numero_afilido':'Numero de afiliado',
            'sexo':'Sexo',
            'fecha_nacimiento':'Fecha de nacimiento',
        }

        widgets={
=======
class pacienteFormu(forms.ModelForm):
    class meta:
        model=Pacientes

        fields = [
            'nombre',
            'apellido',
            'dni',
            'nacionalidad',
            'domicilio',
            'numero_domicilio',
            'cobertura_medica',
            'numero_afilido',
            'sexo',
            'fecha_nacimiento',
        ]

        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'dni': 'Numero de documento',
            'nacionalidad': 'Nacionalidad',
            'domicilio': 'Domicilio',
            'numero_domicilio': 'Numero de domicilio',
            'cobertura_medica': 'Cobertura medica',
            'numero_afilido' : 'Numero de afiliado',
            'sexo': 'Sexo',
            'fecha_nacimiento' : 'Fecha de nacimiento',
        }
        
        widgets = {
>>>>>>> 7927276fd1b2c4dd6dc819fd275d3e6d654cb1e2
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'apellido':forms.TextInput(attrs={'class':'form-control'}),
            'dni':forms.TextInput(attrs={'class':'form-control'}),
            'nacionalidad':forms.TextInput(attrs={'class':'form-control'}),
            'domicilio':forms.TextInput(attrs={'class':'form-control'}),
            'numero_domicilio':forms.TextInput(attrs={'class':'form-control'}),
            'cobertura_medica':forms.TextInput(attrs={'class':'form-control'}),
            'numero_afilido':forms.TextInput(attrs={'class':'form-control'}),
            'sexo':forms.TextInput(attrs={'class':'form-control'}),
            'fecha_nacimiento':forms.DateInput(attrs={'class':'form-control'}),
        }
<<<<<<< HEAD


=======
>>>>>>> 7927276fd1b2c4dd6dc819fd275d3e6d654cb1e2
