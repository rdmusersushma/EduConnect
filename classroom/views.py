from django.shortcuts import render


def home(request):
	return render(request,'classroom/index.html')

def about(request):
	return render(request, 'classroom/about.html')
# Create your views here.
