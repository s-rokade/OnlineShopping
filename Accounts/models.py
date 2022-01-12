from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=30)

    def __str__(s):
        return s.name

class Product(models.Model):
    name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    product_image= models.ImageField(upload_to='product_image/',null=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(s):
        return s.name

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)


class PlaceOrder(models.Model):
    totalBill=models.IntegerField()
    status=models.CharField(max_length=30,default="Processing")
    orderDate=models.DateField(auto_now=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)


#Image model used only In practice

class ImageData(models.Model):
    imgname=models.CharField(max_length=30)
    img=models.ImageField(upload_to='imges', default='')

from django import forms
class ImageForm(forms.ModelForm):
    class Meta:
        model=ImageData
        fields='__all__'