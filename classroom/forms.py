from student_dashboard.models import Student
from Teacher_dashboard.models import Teacher
from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

class UserRegistrationForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2', 'email', 'is_student']

class StudentRegistrationForm(ModelForm):
    class Meta:
        model = Student
        fields = ["department", "reg_no", "contact_number"]

class TeacherRegistrationForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ["department", "qualifications","position", "contact_number"]
