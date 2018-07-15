from django import forms

from .models import Patient

class PatientCreateForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
        'patient_first_name',
        'patient_last_name',
        'praticien_phone_number',
        ]

    # def clean_patient_first_name(self):
    #     patient_first_name = self.cleaned_data.get("patient_first_name")
    #     if patient_first_name == "Monsieur":
    #         raise forms.ValidationError("Not a valid Name")
    #     return patient_first_name
