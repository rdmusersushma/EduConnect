from django.shortcuts import render, redirect
from django.contrib import messages
from .forms  import TeacherRegistrationForm


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
					
# Create your views here.
