from django import forms
from.models import Estudio, Pacientes

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
       # labels = {
        #################################

#crear Formulario de los pacientes.

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


