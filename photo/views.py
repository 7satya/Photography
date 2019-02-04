from django.shortcuts import HttpResponse

# Create your views here.
def home(request):
	return HttpResponse("<h2>Hey ,I am creater.</h2>")
