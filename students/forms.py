from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	course1 = forms.CharField()
	course2 = forms.CharField()
	course3 = forms.CharField()
	contact_number = forms.CharField()
	address = forms.CharField()
	name = forms.CharField()
	GENDER_CHOICES =[
		('M', 'Male'),
		('F', 'Female'),
		('O', 'Other'),
	]
	gender = forms.ChoiceField(choices = GENDER_CHOICES)

	

	class Meta:
		model = User
		fields = ['name', 'email','course1','course2','course3','contact_number','address','gender', 'password1', 'password2']

