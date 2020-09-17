from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import login, authenticate

from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/appone/auth_home")
    else:       # Unregistered User
        return render(request, 'appone/index.html')


class SignUp(FormView):
    success_url = "/appone/auth_home"
    form_class = UserCreationForm
    template_name = "appone/signup.html"

    def form_valid(self, form):
        form.save()
        user = User.objects.get(username=form.data.get('username'))
        login(self.request, user)
        form.save()

        return HttpResponseRedirect("/appone/auth_home")


class SignOut(LogoutView):
    template_name = 'registration/logged_out.html'


class SignIn(LoginView):
    success_url = "/appone/auth_home"
    form_class = AuthenticationForm
    template_name = "appone/signin.html"

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        login(self.request, form.get_user())
        return HttpResponseRedirect("/appone/auth_home")


def home(request):
    user = request.user
    print(type(user))
    if not user.is_authenticated:
        return HttpResponseRedirect("/appone/sign-in")
    return render(request, 'appone/home.html', context={
        'user':user
    })

