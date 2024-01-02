from django import forms
from clinicalApp.models import ClinicData ,Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields='__all__'


class clinicaldataForm(forms.ModelForm):
    class Meta:
        model=ClinicData
        fields='__all__'
        