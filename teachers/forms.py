from django import forms
from Teacher_dashboard.models  import Teacher


class TeacherRegistrationForm(forms.ModelForm):
	
	class Meta:
		model = Teacher
		fields = ['name','email','password','department','position','qualifications','contact_number','address','date_of_birth','gender','subjects_teaching','years_of_experience','profile_picture','additional_notes']


