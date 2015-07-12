import imaplib
import smtplib
import pyttsx
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
#	if request.POST:
#		sender = request.POST.get('Smail')
#		RecieverM = request.POST.get('Rmail')
#		Sub = request.POST.get('Subject')
#		Message = request.POST.get('msg')
#		pwd = request.POST.get('pwd')
#		sender = settings.EMAIL_HOST_USER
#		send_mail(Sub,Message,sender,[RecieverM],fail_silently=False)
#		return HttpResponse("mail sent")
	return render_to_response('index.html')
@csrf_exempt 
def smail(request):
	try:
		if request.POST:
			gmail_user = request.POST.get('Smail')
			gmail_pwd = request.POST.get('pwd')
			FROM = gmail_user
			TO = request.POST.get('Rmail')
			SUBJECT = request.POST.get('Subject')
			TEXT = request.POST.get('msg')
			datavoice = 'You are sening mail to, :' + TO + ', from your email address, :' + gmail_user + ', subject is, :' + SUBJECT + ', and the Message is,:' + TEXT + '. '
			Message = """\From: %s\nTo: %s\nSubject: %s\n\n%s""" % (FROM, TO, SUBJECT, TEXT)
			server = smtplib.SMTP("smtp.gmail.com", 587)
			server.ehlo()
			server.starttls()
			server.login(gmail_user, gmail_pwd)
			server.sendmail(FROM, TO, Message)
			server.close()
			engine = pyttsx.init()
			rate = engine.getProperty('rate')
			engine.setProperty('rate', rate-100)
			engine.say(datavoice)
			engine.runAndWait()
			return render_to_response('sentmail.html')
	
	except:
		return render_to_response('SMError.html')


@csrf_exempt 
def file(request):
	return render_to_response('awm/file.html')

@csrf_exempt 
def login(request):
	try:
		if request.POST:
			msrvr = imaplib.IMAP4_SSL('imap.gmail.com',993)
			username = request.POST.get('uname')
			password = request.POST.get('password')
			msrvr.login(username,password)
			stat,cnt = msrvr.select('inbox')
			stat,dta = msrvr.fetch(cnt[0], '(BODY.PEEK[TEXT])')
			detail = dta[0][1]
			msrvr.close()
			msrvr.logout()
			engine = pyttsx.init()
			rate = engine.getProperty('rate')
			engine.setProperty('rate', rate-100)
			engine.say(detail)
			engine.runAndWait()
			return render_to_response('listenmail.html', { "detail": detail } )
	except:
		return render_to_response('LMError.html')

	
