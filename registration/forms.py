# registration/forms.py

from django import forms
from .models import Student

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'date_of_birth', 'gender', 'highest_qualification', 'blood_group']
