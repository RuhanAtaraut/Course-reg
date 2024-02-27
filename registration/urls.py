# registration/urls.py

from django.urls import path
from .views import registration_form,home,registration_acknowledgment

urlpatterns = [
    path('', home, name='home'),
    path('register/', registration_form, name='registration_form'),
    path('register/acknowledgment/', registration_acknowledgment, name='registration_acknowledgment'),
]
