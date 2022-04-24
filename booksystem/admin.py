from django.contrib import admin
from .models import Flight
from .forms import FlightForm


# custom form management
class FlightAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'leave_city', 'arrive_city', 'leave_airport', 'arrive_airport', 'leave_time', 'arrive_time', 'capacity',
        'price', 'book_sum', 'income')
    form = FlightForm  # Customize what information needs to be entered in the background in the flight form

# Register your models here.
admin.site.register(Flight, FlightAdmin)
