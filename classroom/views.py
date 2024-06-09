from django.shortcuts import render
from django import forms
from formtools.wizard.views import SessionWizardView
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect


def home(request):
	return render(request,'classroom/index.html')

def about(request):
	return render(request, 'classroom/about.html')
# Create your views here.


class UserCreationWizard(SessionWizardView):
    def done(self, form_list, form_dict, **kwargs):
        user = form_list[0]
        student  = form_list[1]
        if user.is_valid() and student.is_valid():
            user.save()
            student.username = user.cleaned_data.get('username')
            student.save()
        else:
            print("either user or student is not valid")
        return HttpResponseRedirect('/slogin')
