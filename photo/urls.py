from django.urls import path
from . import views
from django.contrib.auth.views import login

urlpatterns = [
	path('', views.home, name='home'),
	path('login/', login, {'template_name': 'photo/login.html'}),
]