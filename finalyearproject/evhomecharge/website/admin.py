from django.contrib import admin

from .models import Customer
from .models import Provider
from .models import Booking
from .models import Charger
from .models import Payment
from .models import Invoice
from .models import Contact
from .models import Subscription


admin.site.register(Customer)
admin.site.register(Provider)
admin.site.register(Booking)
admin.site.register(Charger)
admin.site.register(Payment)
admin.site.register(Invoice)
admin.site.register(Contact)
admin.site.register(Subscription)