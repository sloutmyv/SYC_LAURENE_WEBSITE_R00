from django import forms

from .models import Patient

class PatientCreateForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
        'patient_first_name',
        'patient_last_name',
        'patient_phone_number',
        ]

    def __init__(self, *args, **kwargs):
        super(PatientCreateForm, self).__init__(*args, **kwargs)
        self.fields['patient_first_name'].label = "Prénom(s)"
        self.fields['patient_last_name'].label = "Nom(s) de famille"
        self.fields['patient_phone_number'].label = "Téléphone"

    # def clean_patient_first_name(self):
    #     patient_first_name = self.cleaned_data.get("patient_first_name")
    #     if patient_first_name == "Monsieur":
    #         raise forms.ValidationError("Not a valid Name")
    #     return patient_first_name
