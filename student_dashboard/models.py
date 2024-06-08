from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
	is_teacher = models.BooleanField(default=False)
	title = models.CharField(max_length=100)
	email = models.EmailField(default='No address provided')
	department = models.CharField(max_length=100,null=True)
	position = models.CharField(max_length=100,null=True)
	qualifications = models.TextField(default = 'No adderss provided')
	contact_number = models.CharField(max_length=20,default='No contact number provided')
	address = models.TextField(null=True)
	GENDER_CHOICES =[
		('M','Male'),
		('F','Female'),
		('O','Other')
        ]
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
	subjects_teaching = models.CharField(max_length=255,null=True)
	years_of_experience = models.IntegerField(null=True)
	profile_picture = models.ImageField(upload_to='profile_pictures/',blank=True,null=True)
	additional_notes = models.TextField(blank=True,null=True)
	name = models.CharField(max_length=25)
	reg_no = models.CharField(max_length=10)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	user_name = models.ForeignKey(User, on_delete = models.CASCADE)
 
	def __str__(self):
		return self.title

class Department(models.Model):
	department = models.CharField(max_length=100)
	
	def __str__(self):
		return self.name
# Create your models here.
