from django.shortcuts import render
from django.core.mail import send_mail
from Printers import settings
from django.contrib import messages
# Create your views here.
def home(req):
	return render(req,'home.html')

def contact(request):
	if request.method=='POST':
		name=request.POST['name']
		email=request.POST['email']
		subject=request.POST['subject']
		message=request.POST['message']
		sender=settings.EMAIL_HOST_USER
		receiver=settings.EMAIL_HOST_USER
		sub="Reg to your Customer Details..."
		body="""Customer Name:{}\n Customer EmailID: {}\n Subject:{}\n Message:{}\n""".format(name,email,subject,message)
		send_mail(sub,body,sender,[receiver])
		#messages.success(request,'Data Submited Successfully')
	return render(request,'home.html')
