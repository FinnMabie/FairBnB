from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='home'),
    path("sign-up", views.SignUp.as_view(), name="sign-up"),
]