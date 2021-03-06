from django.urls import path, include
from django.contrib.auth import views as auth_views
from project.views import BookListView
from accounts.views import SignUpView


# app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/', include('accounts.urls')),
]

# migrations