from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
	li_no= models.ImageField(upload_to='UserCheck/')
	dob=models.DateField(null=True)
	ph_no=models.CharField(max_length=20)
	pan_no=models.CharField(max_length=20)
	address=models.CharField(max_length=100)
	postal_code=models.CharField(max_length=10)
	city=models.CharField(max_length=10)
	country=models.CharField(max_length=10,default='India')
	p=[(1,'Donor'),(2,'Organisation'),(3,'Guest')]
	role=models.IntegerField(choices=p,default=3)

class Donate(models.Model):
	d=[('Yearly',"Yearly Once"),('Monthly',"Monthly Once"),('Quarterly',"Quarterly Once"),('One Time',"One time donation")]
	s=[('Food',"Food"),('Clothes',"Clothes"),('Money',"Money")]
	p=[('G',"Google pay",'C',"Card",'P',"Paytm")]
	username=models.CharField(max_length=50)
	email=models.EmailField(max_length=50)
	ways_to_donate=models.CharField(max_length=50,choices=d)
	donating_to=models.CharField(max_length=50)
	sponsor_way=models.CharField(max_length=50,choices=s)
	donating_date=models.DateField()
	uid=models.ForeignKey(User,on_delete=models.CASCADE)