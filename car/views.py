from typing import Any
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .import models
from .import forms

# Create your views here.

def show_cars(request):
    cars=models.Car.objects.all()
    brands= models.Brand.objects.all()
    return render(request, 'home.html', {'cars':cars,'brands': brands})

def sort_brand(request, id):
    brand= models.Brand.objects.get(pk=id)
    cars= models.Car.objects.filter(brand=brand)
    return render(request,'sort_brand.html', {'cars': cars,'brands': brand})
    # return redirect('home',{'cars': cars})
    
@login_required
def buy_car(request, id):
    car= models.Car.objects.get(pk=id)
    
    if car.quantity > 0:
        car.quantity-=1
        car.owner= request.user
        # Direct assignment to the reverse side of a related set is prohibited. Use owner.set() instead.
        car.save()
        
    return redirect('detail', id=id)

class CarDetail(DetailView):
    model= models.Car
    template_name='details.html'
    # success_url= reverse_lazy('home')
    pk_url_kwarg='id'
    
    def post(self, request, *args, **kwargs):
        comment_form= forms.CommentForm(request.POST)
        car= self.get_object()
        
        if comment_form.is_valid():
            new_comment= comment_form.save(commit=False)
            new_comment.car= car
            new_comment.name= self.request.user
            new_comment.save()
            return redirect('detail', id=car.id)
        
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        
        context=super().get_context_data(**kwargs)
        car= self.get_object()
        form=forms.CommentForm()
        comments= car.comment.all()
        
        context['form']= form
        context['comments']= comments
        return context
        
        
    
    
 
        

