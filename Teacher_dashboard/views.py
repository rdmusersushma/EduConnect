from django.shortcuts import render

from student_dashboard.models import Post



def home(request):
	context = {
		'info' : Post.objects.all()
	}
	return render(request, 'Teacher_dashboard/home.html', context)
