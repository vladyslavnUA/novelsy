# Learn more or give us feedback
from django.shortcuts import render
from accounts.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView



class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'