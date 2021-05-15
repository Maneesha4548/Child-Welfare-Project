from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class User(AbstractUser):
	li_no= models.ImageField(upload_to='UserCheck/')
	dob=models.DateField(null=True)
	ph_no=models.CharField(max_length=20)
	pan_no=models.CharField(max_length=20)
	address=models.CharField(max_length=100)
	postal_code=models.CharField(max_length=10)
	city=models.CharField(max_length=10)
	state=models.CharField(max_length=10,default='Andra Pradesh')
	country=models.CharField(max_length=10,default='India')
	p=[(1,'Donor'),(2,'Organisation'),(3,'Guest')]
	role=models.IntegerField(choices=p,default=3)

class Donate(models.Model):
	d=[('Yearly',"Yearly Once"),('Monthly',"Monthly Once"),('Quarterly',"Quarterly Once"),('One Time',"One time donation")]
	s=[('Food',"Food"),('Clothes',"Clothes"),('Money',"Money")]
	username=models.CharField(max_length=50)
	email=models.EmailField(max_length=50)
	ways_to_donate=models.CharField(max_length=50,choices=d,default='select')
	donating_to=models.CharField(max_length=50)
	sponsor_way=models.CharField(max_length=50,choices=s,default='select')
	donating_date=models.DateField()
	uid=models.ForeignKey(User,on_delete=models.CASCADE)

class OccDonate(models.Model):
	s=[('Food',"Food"),('Clothes',"Clothes"),('Money',"Money")]
	username=models.CharField(max_length=50)
	email=models.EmailField(max_length=50)
	donating_way=models.CharField(max_length=50,default='On Occasion')
	occ_name=models.CharField(max_length=100)
	donating_to=models.CharField(max_length=50)
	sponsor_way=models.CharField(max_length=50,choices=s,default='select')
	donating_on=models.DateField()
	uid=models.ForeignKey(User,on_delete=models.CASCADE)

class Orgdetails(models.Model):
	org_name=models.CharField(max_length=50,default="Organisation Name")
	found_name=models.CharField(max_length=50,default="Founder Name")
	est_date=models.DateField(null=True)
	no_of_childrens=models.IntegerField(null=True)
	org=models.OneToOneField(User,on_delete=models.CASCADE)

@receiver(post_save,sender=User)
def createpf(sender,instance,created,**kwargs):
	if created:
		Orgdetails.objects.create(org=instance)
		