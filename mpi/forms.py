from django import forms
from.models import Mpi

class formMpi(forms.ModelForm):
    class Meta:
        model=Mpi

        fields = [

            'paciente_mpi',
            's1_rest',
            's2_rest',
            's3_rest',
            's4_rest',
            's5_rest',
            's6_rest',
            's7_rest',
            's8_rest',
            's9_rest',
            's10_rest',
            's11_rest',
            's12_rest',
            's13_rest',
            's14_rest',
            's15_rest',
            's16_rest',
            's17_rest',
            's1_stress',
            's2_stress',
            's3_stress',
            's4_stress',
            's5_stress',
            's6_stress',
            's7_stress',
            's8_stress',
            's9_stress',
            's10_stress',
            's11_stress',
            's12_stress',
            's13_stress',
            's14_stress',
            's15_stress',
            's16_stress',
            's17_stress',
            's1_dif',
            's2_dif',
            's3_dif',
            's4_dif',
            's5_dif',
            's6_dif',
            's7_dif',
            's8_dif',
            's9_dif',
            's10_dif',
            's11_dif',
            's12_dif',
            's13_dif',
            's14_dif',
            's15_dif',
            's16_dif',
            's17_dif',
            'ssr',
            'sss',
            'ssd',
        ]
