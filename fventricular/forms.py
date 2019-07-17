from django import forms
from.models import FuncionVentricular

class ventricularFormu(forms.ModelForm):
    class Meta:
        model=FuncionVentricular # aca indicamos los campos que vamos a utilizar 
        fields= [

            'paciente_fv', 
            'vol_relat_rest', 
            'vfdvi_rest', 
            'fvsvi_rest', 
            'vfdvi_m2_rest', 
            'fvsvi_m2_rest', 
            'frac_eyeccion_rest',  
            'vol_relat_stress', 
            'vfdvi_stress',
            'fvsvi_stress',
            'vfdvi_m2_stress',
            'fvsvi_m2_stress',
            'frac_eyeccion_stress',
            'tid',
        ]