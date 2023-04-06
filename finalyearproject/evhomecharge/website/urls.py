
from django.urls import path
from . import views 
from django.contrib import admin
#from django import forms


urlpatterns = [
    path('home.html',views.home, name="home"),
    path('about.html',views.about, name="about"),
    path('signin.html',views.signin, name="signin"),
    path('news.html',views.news, name="news"),
    path('contact.html',views.contact, name="contact"),
    path('index2.html',views.index2, name="index2"),
    path('portfoliodetails.html',views.portfoliodetails, name="portfoliodetails"),
    path('findaninstaller.html',views.findaninstaller, name="findaninstaller"),
    path('register.html',views.register, name="register"),
    path('signup.html',views.signup, name="signup"),
    path('chargers.html',views.all_charger, name="chargers"),
    path('calendar.html',views.calendar, name="calendar"),
    path('<int:year>/<str:month>/',views.calendar, name="calendar"),
    

    #path('forms/contact.php', views.forms/contact, name="contact_form"),
    #path('forms/signup.php', views.forms/signup, name="signup_form"),
    #path('provider.html',views.provider, name="provider"),
]
