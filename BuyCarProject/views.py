from django.views.generic import TemplateView
from django.shortcuts import render, redirect

class Home(TemplateView):
    template_name= 'home.html'