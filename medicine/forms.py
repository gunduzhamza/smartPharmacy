from .models import *
from django.forms import ModelForm


class PatientForm(ModelForm):

    class Meta:
        model=Patient
        fields=["first_name","last_name","mail"]


class ReceteForm(ModelForm):
    class Meta:
        model=Recete
        fields='__all__'
    

class MedicineForm(ModelForm):
    class Meta:
        model=Medicine
        fields=["ilac_adi","prospekt","ilacfiyati"]
