from django.http import HttpResponseRedirect
from django.db.models import ObjectDoesNotExist
from django.shortcuts import render
from django.contrib.auth import login, authenticate

from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User

from .forms import SearchForm, SaveHomeForm
from .models import Property


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/appone/auth_home")
    else:       # Unregistered User
        return render(request, 'appone/index.html', context={'form':SearchForm()})


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
    if not user.is_authenticated:
        return HttpResponseRedirect("/appone/sign-in")
    return render(request, 'appone/home.html', context={
        'user':user,
        'form':SearchForm()
    })


def search(request):
    query = request.POST.get('search_box')

    try:
        qs = list(Property.objects.filter(address__contains=query))

    except ObjectDoesNotExist:
        print('Object not found')
        qs = None

    return render(request, 'appone/search_results.html', context={'form':SearchForm(), 'qs':qs, 'query':query, 'user':request.user})


def list_saved_homes(request):
    user = request.user
    qs = user.property_set.all()
    return render(request, 'appone/saved_homes.html', context={'form':SearchForm(), 'qs':qs})




def save(request, address=None, query=None):
    if request.user.is_authenticated:
        is_auth = True
    else:
        is_auth = False
    try:
        qs = list(Property.objects.filter(address__contains=query))

    except ObjectDoesNotExist:
        print('Object not found')
        qs = None

    if address:
        address = address.split(',')

        try:
            q = Property.objects.get(
                address=address[0].strip(),
                zip_code=int(address[1].strip())
            )

            if not(request.user in q.user.all()):
                q.user.add(request.user)
                print(str(request.user) + "successfully saved a property.")
        except ObjectDoesNotExist:
            obj = Property.objects.create(
                address=address[0].strip(),
                zip_code=address[1].strip(),
            )
            obj.user.add(request.user)

    return render(request, 'appone/search_results.html', context={'form': SearchForm(), 'qs': qs, 'query': query, 'is_auth':is_auth})








