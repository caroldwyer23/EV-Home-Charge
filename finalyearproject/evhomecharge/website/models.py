from django.db import models

class Customer(models.Model):
	customer_id = models.CharField('Customer ID', max_length=30)
	customer_first_name = models.CharField('Customer First Name', max_length=30)
	customer_last_name =models.CharField('Customer Last Name', max_length=30)
	address = models.CharField('Address',max_length=300)
	county = models.CharField('County', max_length=50)
	eircode = models.CharField('Eircode', max_length=30)
	phone = models.CharField ('Contact Phone', max_length=15)
	email = models.EmailField('Customer Email',max_length=100)
	charger_type = models.CharField('Charger Type',max_length=40)
	car_type = models.CharField('Car Type',max_length=40)


	def __str__(self):
		return self.customer_first_name +''+ self.customer_last_name



class Provider(models.Model):
	provider_id =models.CharField('Provider ID',max_length=30)
	first_name = models.CharField('Provider First Name', max_length=30)
	last_name =models.CharField('Provider Last Name', max_length=30)
	address = models.CharField('Address',max_length=300)
	county = models.CharField('County', max_length=50)
	eircode = models.ForeignKey('Eircode', blank=True, null = True, on_delete=models.CASCADE) 
	phone = models.CharField ('Contact Phone', max_length=40)
	email = models.EmailField('Provider Email',max_length=40)
	charger_id = models.CharField('Charger_id',max_length= 40)
	charger_type = models.CharField('Charger Type',max_length=40)

	def __str__(self):
		return self.first_name +''+ self.last_name



class Booking(models.Model):
	booking_id = models.CharField('Booking ID', max_length=30)
	customer_id = models.ForeignKey('Customer ID', blank=True, null = True, on_delete=models.CASCADE)
	name = models.CharField('Booking Name',max_length=120)
	booking_date = models.DateTimeField('Booking Date', max_length=40)
	provider_id =models.ForeignKey('Provider ID',blank=True, null = True, on_delete=models.CASCADE)
	arrival_time =models.DateTimeField('Arrival Time', max_length=30)
	departure_time =models.DateTimeField('Departure Time', max_length=30)
	charger_type = models.ForeignKey('Charger Type',blank=True, null = True, on_delete=models.CASCADE)
	car_type = models.ForeignKey('Car Type',blank=True, null = True, on_delete=models.CASCADE)

	def __str__(self):
		return self.booking_id + ''+ self.booking_date



class Charger(models.Model):
	charger_id = models.CharField('Charger ID', max_length=30)
	provider_id =models.ForeignKey('Provider ID', blank=True, null = True, on_delete=models.CASCADE) 
	charger_type = models.CharField('Charger Type',max_length = 100) 
	booking_date = models.DateTimeField('Booking Date',max_length=30)
	eircode = models.ForeignKey('Eircode', blank=True, null = True, on_delete=models.CASCADE) 
	voltage = models.CharField('Voltage',max_length=100)
	description = models.TextField('Description',max_length= 100)
	booking_date = models.DateTimeField('Booking Date',max_length=30)
	customerusers = models.ManyToManyField('Customer',max_length= 100)


	def __str__(self):
		return self.charger_type



class Payment(models.Model):
	payment_id = models.CharField('Payment ID', max_length= 120)
	booking_id = models.CharField('Booking ID', max_length=30)
	customer_id = models.ForeignKey('Customer ID', blank=True, null = True, on_delete=models.CASCADE)
	provider_id = models.ForeignKey('Provider ID',blank=True, null = True, on_delete=models.CASCADE)
	charger_id = models.ForeignKey('Charger ID', blank=True, null = True, on_delete=models.CASCADE)
	payment_type = models.CharField('Payment Type', max_length=30)
	payment_date = models.TextField('Payment Date', max_length =30)
	
	def __str__(self):
		return self.payment_type



class Invoice(models.Model):
	invoice_id = models.CharField('Invoice ID', max_length= 120)
	booking_id = models.ForeignKey('Booking ID', blank=True, null = True, on_delete=models.CASCADE)
	payment_id = models.ForeignKey('Payment ID', blank=True, null = True, on_delete=models.CASCADE)
	provider_id = models.ForeignKey('Provider ID',blank=True, null = True, on_delete=models.CASCADE)
	charger_id = models.ForeignKey('Charger ID', blank=True, null = True, on_delete=models.CASCADE)
	customer_id = models.ForeignKey('Customer ID', blank=True, null = True, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.invoice_id + ''+ self.booking_date


#===============================================================#

class Subscription(models.Model):
	email = models.EmailField('Subscription Email',max_length=100)
	
	def __str__(self):
		return self.email
#==============================================================#

class Contact(models.Model):
	name = models.CharField('User Name', max_length=120)
	email = models.EmailField('Email',max_length=100)
	subject = models.TextField('Subject',max_length=100)
	message = models.TextField('Subject',max_length=100)
	
	def __str__(self):
		return self.name 

#===============================================================#

