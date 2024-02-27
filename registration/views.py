# registration/views.py

from django.shortcuts import render, redirect
from .models import Student
from .forms import RegistrationForm


def home(request):
    return render(request, 'home.html')
def registration_form(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_acknowledgment')  # Redirect after successful form submission
    else:
        form = RegistrationForm()

    return render(request, 'registration_form.html', {'form': form})
def registration_acknowledgment(request):
    return render(request, 'registration_acknowledgment.html')
