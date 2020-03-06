from django.urls import path, include
from django.contrib.auth import views as auth_views
from project.views import BookListView
from accounts.views import SignUpView


app_name = 'accounts'

urlpatterns = [
    path('list_of_books/', BookListView.as_view(), name='accounts'),
    path('login/', auth_views.LoginView.as_view(template_name="accounts/login.html"), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
]
