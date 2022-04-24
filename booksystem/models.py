from django.contrib.auth.models import Permission, User
from django.db import models


# Create your models here.
# Adding a primary key will overwrite the default primary key
class Flight(models.Model):
    user = models.ManyToManyField(User, default=1)  # With this field, the default background addition is invalid, you must customize the form to remove this field
    name = models.CharField(max_length=100)  # Flight China Southern Airlines CZ3969
    leave_city = models.CharField(max_length=100, null=True)  # leave the city
    arrive_city = models.CharField(max_length=100, null=True)  # arrival city
    leave_airport = models.CharField(max_length=100, null=True)  # departure airport
    arrive_airport = models.CharField(max_length=100, null=True)  # Arrival airport
    leave_time = models.DateTimeField(null=True)  # Date time field includes date field information and adds time
    arrive_time = models.DateTimeField(null=True)
    capacity = models.IntegerField(default=0, null=True)  # total number of seats
    price = models.FloatField(default=0, null=True)  # price
    book_sum = models.IntegerField(default=0, null=True)  # Total number of bookings
    income = models.FloatField(default=0, null=True)  # income

    def __str__(self):
        return self.name
