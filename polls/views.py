from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("<h1>You got to my homepage, congrats. You musst be a master of the internet.</h1>")
