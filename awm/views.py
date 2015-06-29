from django.shortcuts import render, render_to_response
from django.template import Context, Template
from django.template import RequestContext, loader
from django.core.context_processors import csrf
from django.template import RequestContext, loader
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings 


@csrf_exempt 
def index(request):
	if request.POST:
		sender = request.POST.get('Smail')
		RecieverM = request.POST.get('Rmail')
		Sub = request.POST.get('Subject')
		Message = request.POST.get('msg')
		pwd = request.POST.get('pwd')
		sender = settings.EMAIL_HOST_USER
		send_mail(Sub,Message,sender,[RecieverM],fail_silently=False)
		return HttpResponse("mail sent")
	return render_to_response('index.html')

@csrf_exempt 
def file(request):
	return render_to_response('awm/file.html')
@csrf_exempt 
def send(request):
	pass
	
