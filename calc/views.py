from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def add(request):
	num1 = int(request.GET['a'])
	num2 = int(request.GET['b'])
	result = num1 + num2
	return HttpResponse(result)