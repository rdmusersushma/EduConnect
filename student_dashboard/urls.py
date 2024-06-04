from django.urls import path
from . import views

urlpatterns = [
    path('sprofile/', views.profile,name='s-profile'),
    path('home/', views.home, name='s-home'),
]

