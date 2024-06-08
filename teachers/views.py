from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms  import TeacherRegistrationForm
from student_dashboard.models import Department

def tregister(request):
	if request.method == 'POST':
	
		form = TeacherRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('name')
			messages.success(request, f'Hi.. {username}! Wellcome to Educonnect ')
			return redirect('t-home')
	else:
		form = TeacherRegistrationForm()
	return render(request, 'teachers/tregister.html',{'form': form})
					
def tlogin(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['name']
			department = form.cleaned_data['department']
			user = authenticate(request, username=username, password = password)
			
			if user is not None:
				login(request,user)
				if user.is_teacher:
					return redirect('tdepartment')
				else:
					return redirect('student_dashboard')
			else:
				pass
		else:
			pass
	else:
		form = LoginForm()
	return render(request, 'login.html',{'form':form})

def tdepartment(request):
	
	return render(request, 'teachers/tdepartment.html')
# Create your views here.
