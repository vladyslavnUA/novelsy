from django.shortcuts import render
from accounts.forms import UserCreationForm
from accounts.forms import SignUpForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
# from .models import UserProfile
# from .forms import UserProfileForm
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.detail import (DetailView)
from django.contrib.auth.models import User
from django.views.generic.edit import (
    CreateView,
    # UserProfile
)

class SignUpView(SuccessMessageMixin, CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'registration/signup.html'
    success_message = (
        '''congratulations! you are now a registered user.'''
    )
    
    # def form_valid(self, form):
    #     self.object = form.save()
    #     return super().form_valid(form)