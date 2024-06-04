from django.shortcuts import render
from .models import Post

def home(request):
	return render(request, 'student_dashboard/Home.html')
def profile(request):
	context = {
		'posts':Post.objects.all()
		}
	return render(request,'student_dashboard/profile.html',context)
# Create your views here.
