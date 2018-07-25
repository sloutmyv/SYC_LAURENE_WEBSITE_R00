from django import forms


from .models import Patient

class PatientCreateForm(forms.ModelForm):
    patient_birthday = forms.DateField(required=False, widget=forms.DateInput(format='%d/%m/%Y'),input_formats=('%d/%m/%Y', ))

    class Meta:
        model = Patient
        fields = [
        'patient_first_name',
        'patient_last_name',
        'patient_maiden_name',
        'patient_birthday',
        'patient_phone_number',
        'patient_address',
        'patient_zip_code',
        'patient_city',
        'patient_contry',
        'patient_situation',
        'patient_job',
        'patient_gyn',
        'patient_med',
        ]

    def __init__(self, *args, **kwargs):
        super(PatientCreateForm, self).__init__(*args, **kwargs)
        self.fields['patient_first_name'].label = "Prénom(s)"
        self.fields['patient_last_name'].label = "Nom(s) de famille"
        self.fields['patient_maiden_name'].label = "Nom(s) de jeune fille"
        self.fields['patient_birthday'].label = "Date de naissance"
        self.fields['patient_phone_number'].label = "Téléphone"
        self.fields['patient_address'].label = "Adresse"
        self.fields['patient_zip_code'].label = "Code postal"
        self.fields['patient_city'].label = "Ville"
        self.fields['patient_contry'].label = "Pays"
        self.fields['patient_situation'].label = "Situation personnelle"
        self.fields['patient_job'].label = "Profession"
        self.fields['patient_gyn'].label = "Gynécologue"
        self.fields['patient_med'].label = "Médecin traitant"

    # def clean_patient_first_name(self):
    #     patient_first_name = self.cleaned_data.get("patient_first_name")
    #     if patient_first_name == "Monsieur":
    #         raise forms.ValidationError("Not a valid Name")
    #     return patient_first_name
