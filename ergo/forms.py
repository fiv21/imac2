from django import forms
from.models import Ergometria
class FormularioErgometria(forms.ModelForm):
    
    class Meta:
        model = Ergometria
        fields = (
            'paciente_ergo',
            'ciclo_ergo',
            'banda_ergo',
            'carga',
            'fc_basal', 
            'tas_basal', 
            'tad_basal', 
            'fc_esfuerzo',
            'tas_esfuerzo', 
            'tad_esfuerzo', 
            'mets', 
            'st', 
            'st_mm', 
            'ta_plana', 
            'motivo_suspencion',
            'arritmia_sv',
            'arritmia_v',
            'sintomas',
            'fcm_edad',
            'percent_fcmp', 
            'itt',)
