from django.contrib.auth import views as auth_view
from django.contrib.auth.forms import AuthenticationForm


class LoginView(auth_view.LoginView):
    form_class = AuthenticationForm
    template_name = "accounts/login.html"
    redirect_authenticated_user = True


class LogoutView(auth_view.LogoutView):
    pass
