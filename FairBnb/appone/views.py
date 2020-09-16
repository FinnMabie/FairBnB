from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    context = {
        'test':1,
        'user':'finn'
    }
    return render(request, 'appone/index.html', context=context)


class SignUp(FormView):
    success_url = "/appone/"
    form_class = UserCreationForm
    template_name = "appone/signup.html"

    def form_valid(self, form):
        print(form)
        form.save()
        return super().form_valid(form)
