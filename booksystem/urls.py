"""FlightTicket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import re_path as url, include
from . import views

app_name = 'booksystem'  # Add this property to facilitate jinja syntax

urlpatterns = [
    # Register and Login
    url(r'^register/$', views.register, name='register'),  # register
    url(r'^login_user/$', views.login_user, name='login_user'),  # login
    url(r'^logout_user/$', views.logout_user, name='logout_user'),  # Sign out

    # main page
    url(r'^$', views.index, name='index'),  # welcome page
    url(r'^result/$', views.result, name='result'),  # search results
    url(r'^user_info/$', views.user_info, name='user_info'),  # User Info
    url(r'^book/flight/(?P<flight_id>[0-9]+)/$', views.book_ticket, name='book_ticket'),  # booking
    url(r'^refund/flight/(?P<flight_id>[0-9]+)/$', views.refund_ticket, name='refund_ticket'),  # refund
]
