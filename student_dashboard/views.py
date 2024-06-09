from django.shortcuts import render
from .models import Student

def home(request):
	return render(request, 'student_dashboard/Home.html')
def profile(request):
	context = {
		'posts':Student.objects.all()
		}
	return render(request,'student_dashboard/profile.html',context)
# Create your views here.
