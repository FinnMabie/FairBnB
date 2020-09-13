from django.shortcuts import render

def index(request):
    context = {
        'test':1,
        'user':'finn'
    }
    return render(request, 'appone/index.html', context=context)
# Create your views here.
