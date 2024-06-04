from django.shortcuts import render

from .models import Teacher



def home(request):
	context = {
		'info' : Teacher.objects.all()
	}
	return render(request, 'Teacher_dashboard/home.html', context)
