from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from student_dashboard.models import Department



class TeacherRegistrationForm(UserCreationForm):
	email = forms.EmailField()
	address = forms.CharField()
	name = forms.CharField()
	GENDER_CHOICES =[
		('M', 'Male'),
		('F', 'Female'),
		('O', 'Other'),
	]
	gender = forms.ChoiceField(choices = GENDER_CHOICES)
	subjects_teaching = forms.CharField()
	contact_number = forms.CharField()
	years_of_experience = forms.IntegerField()
	profile_picture = forms.ImageField()

	class Meta:
		model = User
		fields = ['name', 'email','contact_number','address','gender','subjects_teaching','years_of_experience','profile_picture', 'password1', 'password2']

class LoginForm(UserCreationForm):
	name = forms.CharField()
	department = forms.ModelChoiceField(queryset=Department.objects.all())
	
	class Meta:
		model = User
		fields =[ 'name', 'department']

