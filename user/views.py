from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout
from django.views.generic import CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .import forms
from django.views.generic import TemplateView
# Create your views here.

class UserSignup(CreateView):
    model=User
    form_class=forms.SignupForm
    template_name='login.html'
    success_url= reverse_lazy('user_login')

class UserLogin(LoginView):
    model= User
    form_class = AuthenticationForm
    template_name='login.html'
    success_url= reverse_lazy('home')
    
def user_logout(request):
    logout(request)
    return redirect('home')
    
    
def profile(request):
    user= request.user
    cars= user.owned.all()
    
    return render(request, 'profile.html', {'cars':cars})
    
    