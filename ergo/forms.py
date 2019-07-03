from django import forms
from.models import Ergometria

class FormErgometria(forms.ModelForm):

    class meta:
        model=Ergometria
    
        fields = [
            'paciente_ergo',            #=models.ForeignKey(Pacientes,null=True,on_delete=models.CASCADE)
            'ciclo_ergo',               #=models.BooleanField(default=False)
            'banda_ergo',               #=models.BooleanField(default=False)
            'carga',                    #= models.IntegerField (verbose_name="Carga",null=True)
            'fc_basal',                 #= models.IntegerField (verbose_name="Fc basal",null=True)
            'tas_basal',                #= models.IntegerField(verbose_name="Tas basal",null=True)
            'tad_basal',                #= models.IntegerField(verbose_name="Tad basal",null=True)
            'fc_esfuerzo',              #= models.IntegerField(verbose_name="Fc esfuerzo",null=True)
            'tas_esfuerzo',             #= models.IntegerField(verbose_name="Tas esfuerzo",null=True)
            'tad_esfuerzo',             #= models.IntegerField(verbose_name="Tad esfuerzo",null=True)
            'mets',                     #= models.IntegerField(verbose_name="Mets",null=True)
            'st',                       #= models.CharField(max_length=50)
            'st_mm',                    #= models.IntegerField(verbose_name="St mm",null=True)
            'ta_plana',                 #= models.BooleanField(default=False)
            'motivo_suspencion',        #=models.CharField(max_length=50)
            'arritmia_sv',              #=models.CharField(max_length=50)
            'arritmia_v',               #=models.CharField(max_length=50)
            'sintomas',                 #=models.CharField(max_length=50)
            'fcm_edad',                 #= models.IntegerField(verbose_name="Fcm edad",null=True)
            'percent_fcmp',             #= models.IntegerField(verbose_name="Percent fcmp",null=True)
            'itt',                      #= models.IntegerField(verbose_name="Itt",null=True)
        ]

        labels = {
            'paciente_ergo':'Paciente',
            'ciclo_ergo':'Ciclo ergo',
            'banda_ergo':'Banda ergo',
            'carga':'Carga',
            'fc_basal':'Fc basal',
            'tas_basal':'Tas basal', 
            'tad_basal':'Tad basal',
            'fc_esfuerzo':'Fc esfuerzo',
            'tas_esfuerzo':'Tas esfuerzo',
            'tad_esfuerzo':'Tad esfuerzo',
            'mets':'Mets',
            'st':'St',
            'st_mm':'St mm',
            'ta_plana':'Ta plana',
            'motivo_suspencion':'Motivo de suspencion',
            'arritmia_sv':'Arritmia',
            'arritmia_v':'Arritmia v',
            'sintomas':'Sintomas',
            'fcm_edad':'Fcm edad',
            'percent_fcmp':'Percent fcmp',
            'itt':'Itt',
        }

       