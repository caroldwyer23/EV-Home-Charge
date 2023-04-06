from django.shortcuts import render
from .models import Customer
from .models import Provider
from .models import Booking
from .models import Charger
from .models import Payment
from .models import Invoice
from .models import Contact
from .models import Subscription
from django.http import HttpResponseRedirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime



def calendar(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
	month = month.capitalize()
	time = datetime.now().strftime('%H:%M:%S')
	
	
#get current year
	now = datetime.now()
	current_year = now.year

	#create a calendar
	html_cal = HTMLCalendar().formatmonth(now.year, now.month)
	

	return render(request,'calendar.html',{
		"year": year,
		"month": month,
		"calendar":html_cal,
		"current_year": current_year,
		"time":time,

		})

def about(request):
	return render(request, 'about.html', {})

def home(request):
	return render(request, 'home.html', {})

def blogsingle(request):
	return render(request, 'blogsingle.html', {})

def all_charger(request):
	charger_list = Charger.objects.all()
	return render(request,'chargers/charger_list.html',{
		"charger_list": charger_list})

def contact(request):
	return render(request, 'contact.html', {})

#def formcontact(request):
	#return render(request, 'form/contact.php', {})

def news(request):
	return render(request, 'news.html', {})

def signin(request):
	return render(request, 'signin.html', {})

def index2(request):
	return render(request, 'index2.html', {})

def portfoliodetails(request):
	return render(request, 'portfoliodetails.html', {})

def findaninstaller(request):
	return render(request, 'findaninstaller.html', {})

def provider(request):
	provider = Provider.objects.all()
	return render(request, 'provider.html', 
		{'provider': provider})

def register(request):
	return render(request, 'register.html', {})

def signup(request):
	return render(request, 'signup.html',{})
	#submitted = False
	#if request.method == 'POST':
		#form = signup(request.Post)
		#if form.is_valid():
			#form.save()
			#return HttpResponseRedirect('/signup?submitted=True')
	#else:
		#form = signup
		#if 'submitted' in request.GET:
			#submitted = True

	#return render(request, 'signup.html', {'form':form, 'submitted':submitted})


		#name = request.POST['Name']
		#password = request.POST['Password']
	#return render(request, 'signup.html', {})

def charger(request):
	charger_list = Charger.objects.all()
	return render(request, 'charger.html',{'charger_list':charger_list})

