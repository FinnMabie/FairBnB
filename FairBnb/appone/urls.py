from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='home'),
    path("sign-up", views.SignUp.as_view(), name="sign-up"),
    path("sign-in", views.SignIn.as_view(), name="sign-in"),
    path("auth_home", views.home, name="auth_home"),
    path("signout", views.SignOut.as_view(), name='sign-out')

]