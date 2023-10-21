from django.shortcuts import render, HttpResponse
from django.views import generic
from django.urls import reverse_lazy

from . import forms

# Create your views here.

class RegisterView(generic.CreateView):
    template_name = "registration/register.html"
    form_class = forms.RegisterUserForm
    success_url = reverse_lazy("login")