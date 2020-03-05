from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    '''A form that handles registering new users.'''
    class Meta:
        model = User
        fields = ['email', 'username',
                  'first_name', 'last_name',
                  'password1', 'password2'
                  ]

    def save(self, commit=True):
        '''Initializes fields of the new User instance.'''
        user = super(SignUpForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

# class UserCreationForm(UserCreationForm):
#     email = forms.EmailField(required=True, label='Email')

#     class Meta:
#         model = User
#         fields = ("username", "email", "password1", "password2")

#     def save(self, commit=True):
#         user = super(UserCreationForm, self).save(commit=False)
#         user.email = self.cleaned_data["email"]
#         if commit:
#             user.save()
#         return user