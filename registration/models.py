from django.db import models

# Create your models here.
# registration/models.py

from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    course_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    date_of_birth = models.DateField(blank= True,null=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')],default='Unknown')
    highest_qualification = models.CharField(max_length=100,default='Unknown')
    blood_group = models.CharField(max_length=5, default='Unknown')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

