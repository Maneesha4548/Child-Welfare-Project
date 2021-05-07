from django import forms
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from App.models import User,Donate,OccDonate

class UsrReg(UserCreationForm):
	password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Create New Password"}))
	password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Confirm New Password"}))
	class Meta:
		model=User
		fields=["username","email"]
		widgets={
		"username":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Username",
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control",
			"placeholder":"Email ID",
			}),
		}

class UsPerm(forms.ModelForm):
	class Meta:
		model=User
		fields=["username","role"]
		widgets={
		"username":forms.TextInput(attrs={
			"class":"form-control",
			"readOnly":True,
			}),
		"role":forms.Select(attrs={
			"class":"form-control",
			}),
		}

class DonateForm(forms.ModelForm):
	class Meta:
		model=Donate
		fields=["ways_to_donate","donating_to","sponsor_way","donating_date"]
		widgets={
		"ways_to_donate":forms.Select(attrs={
			"class":"form-control",
			"required":True,
			}),
		"donating_to":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Organisation Name",
			"required":True,
			}),
		"sponsor_way":forms.Select(attrs={
			"class":"form-control",
			"required":True,
			}),
		"donating_date":forms.DateInput(attrs={
			"class":"form-control",
			"placeholder":"Enter the date of donation",
			"required":True,
			}),

		}

class UpdateForm(forms.ModelForm):
	class Meta:
		model = Donate
		fields=["ways_to_donate","donating_to","sponsor_way","donating_date"]
		widgets={
		"ways_to_donate":forms.Select(attrs={
			"class":"form-control",
			"required":True,
			}),
		"donating_to":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Organisation Name",
			"required":True,
			}),
		"sponsor_way":forms.Select(attrs={
			"class":"form-control",
			"required":True,
			}),
		"donating_date":forms.DateInput(attrs={
			"class":"form-control",
			"placeholder":"Enter the date of donation",
			"required":True,
			}),

		}

class UpForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username","email","dob","ph_no","pan_no","address","postal_code","city","country"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control",
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control",
			"placeholder":"Email id",
			"required":True,
			}),
		"dob":forms.DateInput(attrs={
			"class":"form-control",
			"placeholder":"Select your date of birth",
			"required":True,
			}),
		"ph_no":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"Enter your Mobile Number",
			"required":True,
			}),
		"pan_no":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter your PAN Number",
			}),
		"address":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Your Full Address",
			"required":True,
			}),
		"postal_code":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Your PIN Code",
			"required":True,
			}),
		"city":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Your city",
			"required":True,
			}),
		"country":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Your Country",
			"required":True,
			}),
		}

class ChpasForm(PasswordChangeForm):
	old_password=forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control",
		"placeholder":"Enter Old password"
		}))
	new_password1=forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control",
		"placeholder":"Enter New password"
		}))
	new_password2=forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control",
		"placeholder":"Confirm New password"
		}))

	class Meta:
		model=User
		fields=['oldpassword','newpassword','confirmpassword']


class OccDonateForm(forms.ModelForm):
	class Meta:
		model=OccDonate
		fields=["occ_name","donating_to","sponsor_way","donating_on"]
		widgets={
		"occ_name":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Occasion Name",
			"required":True,
			}),
		"donating_to":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Organisation Name",
			"required":True,
			}),
		"sponsor_way":forms.Select(attrs={
			"class":"form-control",
			"required":True,
			}),
		"donating_on":forms.DateInput(attrs={
			"class":"form-control",
			"placeholder":"Enter the date of donation",
			"required":True,
			}),

		}

