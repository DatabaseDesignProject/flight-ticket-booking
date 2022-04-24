from django import forms
from django.contrib.auth.models import User
from .models import Flight


class PassengerInfoForm(forms.Form):
    leave_city = forms.CharField(label='leave_city', max_length=100)
    arrive_city = forms.CharField(label='arrive_city', max_length=100)
    leave_date = forms.DateField(label='leave_date')


# Input information for custom flight object
class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        exclude = ['user']  # User information cannot be entered from the background


# Fields that the user needs to enter
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
