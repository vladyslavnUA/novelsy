from django.shortcuts import render
from accounts.forms import UserCreationForm
from accounts.forms import SignUpForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.detail import (DetailView)
from django.contrib.auth.models import User
from django.views.generic.edit import (
    CreateView,
    UserProfile
)



class SignUpView(SuccessMessageMixin, CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'registration/signup.html'
    success_message = (
        '''congradulations! you are now a registered user.'''
    )
    
    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)


class UserProfile(UserPassesTestMixin, DetailView):
    model = User
    template_name = 'accounts/profile/show_profile.html'

    def get_queryset(self):
        '''Returns a queryset of all User objects.'''
        return self.model.objects.all()

    def get(self, request, pk):
        """Renders a page to show an account of user.
           Parameters:
           pk(int): specific id of the User in db.
           request(HttpRequest): the HTTP request sent to the server

           Returns:
           render: HttpResponse

         """
        user = self.get_queryset().get(id=pk)
        context = {
            'user': user,
        }
        return render(request, self.template_name, context)

    def test_func(self):
        '''Ensures the user can see only their own profile.'''
        requested_user = self.get_object()
        user = self.request.user
        return requested_user == user


# class ProfileUpdate(UserPassesTestMixin, UpdateView):
#     model = ArchitectOrOfficer
#     form_class = StatusForm
#     template_name = 'accounts/profile/update.html'

#     def get_queryset(self):
#         '''Returns a queryset of all User objects.'''
#         return UserProfile.objects.all()

#     def get(self, request, pk):
#         """Renders a page for user to check off if they're an architect or
#            compliance officer.

#            Parameters:
#            pk(int): specific id of the User in db.
#            request(HttpRequest): the HTTP request sent to the server

#            Returns:
#            render: HttpResponse

#          """
#         status = self.get_queryset().get(id=pk)
#         user = User.objects.get(id=status.user.id)
#         context = {
#             'user': user,
#         }
#         return super().get(request)

#     def test_func(self):
#         '''Ensures the user can see only their own profile.'''
#         requested_user = self.get_object().user
#         user = self.request.user
#         return requested_user == user
# class ProfileDelete(self):
#     pass