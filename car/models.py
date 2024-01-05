from django.db import models
from brand.models import Brand
from django.contrib.auth.models import User

# Create your models here.
class Car(models.Model):
    name= models.CharField(max_length=40)
    brand= models.ForeignKey(Brand, on_delete=models.CASCADE)
    image= models.ImageField(upload_to='car/media/uploads')
    description= models.TextField()
    price=models.IntegerField()
    quantity= models.IntegerField()
    owner= models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name= 'owned')
    buy_date=models.DateField(auto_now_add=True, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class Comment(models.Model):
    name= models.CharField(max_length=30, blank=True, null= True)
    text=models.TextField()
    car=models.ForeignKey(Car, on_delete=models.CASCADE, related_name= 'comment')
    
