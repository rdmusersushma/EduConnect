"""
URL configuration for educonnect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from students import views as student_views
from teachers import views as teacher_views
from classroom.views import UserCreationWizard
from classroom.forms import UserRegistrationForm, StudentRegistrationForm, TeacherRegistrationForm 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', UserCreationWizard.as_view([UserRegistrationForm, StudentRegistrationForm]), name='register'),
    # path('sregister/', student_views.register, name='sregister'),
    # path('tregister/', teacher_views.tregister, name='tregister'),
    path('tdepartment/', teacher_views.tdepartment, name = 'tdepartment'),
    path('slogin/', auth_views.LoginView.as_view(template_name='students/login.html',next_page='/student/sprofile'), name='slogin'),
    path('slogin/', auth_views.LoginView.as_view(template_name='students/login.html',next_page='/student/sprofile'), name='slogin'),
    path('slogout/', auth_views.LogoutView.as_view(template_name='students/logout.html'), name='slogout'),
    path('tlogin/', auth_views.LoginView.as_view(template_name='teachers/login.html', next_page='/teacher'), name = 'tlogin'),
   # path('tlogout/', auth_views.LoginView.as_view(template_name='teachers/logout.html'),name='tlogout'),
    path('', include('classroom.urls')),
    path('student/',include('student_dashboard.urls')),
    path('teacher/',include('Teacher_dashboard.urls')),
    #path('',include('teachers.urls')),
   
   
]
