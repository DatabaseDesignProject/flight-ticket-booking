from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from .forms import PassengerInfoForm, UserForm
from .models import Flight
from .classes import IncomeMetric, Order
from django.contrib.auth.models import Permission, User
import datetime, pytz
from operator import attrgetter

ADMIN_ID = 1


# Administrator background financial management
# Statistics on the weekly, monthly and annual operating income of airlines.
def admin_finance(request):
    all_flights = Flight.objects.all()
    all_flights = sorted(all_flights, key=attrgetter('leave_time'))  # Sort all flights by departure time

    # Label daily entry of flights with different time labels [week, month, day]
    week_day_incomes = []
    month_day_incomes = []
    year_day_incomes = []

    # Use set to store all weeks, months, and years
    week_set = set()
    month_set = set()
    year_set = set()
    for flight in all_flights:
        if flight.income > 0:  # Only count flights with revenue
            # tag last week
            this_week = flight.leave_time.strftime('%W')  # Datetime get week
            week_day_incomes.append((this_week, flight.income))  # add tuple(week, income)
            week_set.add(this_week)
            # label last month
            this_month = flight.leave_time.strftime('%m')  #Datetime get month
            month_day_incomes.append((this_month, flight.income))  #Add tuple (month, income)
            month_set.add(this_month)
            #label last year
            this_year = flight.leave_time.strftime('%Y')  #Datetime get year
            year_day_incomes.append((this_year, flight.income))  #Add tuple (year, income)
            year_set.add(this_year)

    # Store weekly income
    # Store weekly income in the week_incomes List using the IncomeMetric type
    week_incomes = []
    for week in week_set:
        income = sum(x[1] for x in week_day_incomes if x[0] == week) # Sum the income of the same week
        flight_sum = sum(1 for x in week_day_incomes if x[0] == week) # The total number of flights in the same week
        week_income = IncomeMetric(week, flight_sum, income) # Store the data in the IncomeMetric class, which is convenient for jinja syntax
        week_incomes.append(week_income)
    week_incomes = sorted(week_incomes, key=attrgetter('metric')) # Arrange the week_incomes of the List type in ascending order of weeks

 # store monthly income
    # Store the monthly income in the month_incomes List using the IncomeMetric type
    month_incomes = []
    for month in month_set:
        income = sum(x[1] for x in month_day_incomes if x[0] == month)
        flight_sum = sum(1 for x in month_day_incomes if x[0] == month)
        month_income = IncomeMetric(month, flight_sum, income)
        month_incomes.append(month_income)
    month_incomes = sorted(month_incomes, key=attrgetter('metric')) # Sort the month_incomes of the List type in ascending order by month

    # store annual income
    # Store the annual income in the year_incomes List using the IncomeMetric type
    year_incomes = []
    for year in year_set:
        income = sum(x[1] for x in year_day_incomes if x[0] == year)
        flight_sum = sum(1 for x in year_day_incomes if x[0] == year)
        year_income = IncomeMetric(year, flight_sum, income)
        year_incomes.append(year_income)
    year_incomes = sorted(year_incomes, key=attrgetter('metric')) # Sort the year_incomes of the List type in ascending order by year

    # store order information
    passengers = User.objects.exclude(pk=1) # remove the administrator
    order_set = set()
    for p in passengers:
        flights = Flight.objects.filter(user=p)
        for f in flights:
            route = f.leave_city + ' → ' + f.arrive_city
            order = Order(p.username, f.name, route, f.leave_time, f.price)
            order_set.add(order)

    # information to the front end
    context = {
        'week_incomes': week_incomes,
        'month_incomes': month_incomes,
        'year_incomes': year_incomes,
        'order_set': order_set
    }
    return context


# Display user order information
# flight information, refund management
def user_info(request):
    if request.user.is_authenticated:
        # If the user is an admin, render the company flight revenue statistics page admin_finance
        if request.user.id == ADMIN_ID:
            context = admin_finance(request)  # Get the data to pass to the front end
            return render(request, 'booksystem/admin_finance.html', context)
        # If the user is a normal user, render the user's ticket information user_info
        else:
            booked_flights = Flight.objects.filter(user=request.user)  # Filter out the flights booked by this user from the booksystem_flight_user table
            context = {
                'booked_flights': booked_flights,
                'username': request.user.username,  # Navigation bar information update
            }
            return render(request, 'booksystem/user_info.html', context)
    return render(request, 'booksystem/login.html')  # If the user is not logged in, render the login page

#Home
#A booking page in the nature of a welcome page
def index(request):
    return render(request, 'booksystem/index.html')


#exempt from csrf
@csrf_exempt
def book_ticket(request, flight_id):
    if not request.user.is_authenticated:  #Render login page if not logged in
        return render(request, 'booksystem/login.html')
    else:
        flight = Flight.objects.get(pk=flight_id)
        #View the flights that passengers have ordered
        booked_flights = Flight.objects.filter(user=request.user)  #return QuerySet

        if flight in booked_flights:
            return render(request, 'booksystem/book_conflict.html')

        #After confirming book_flight.html, the request is the POST method. Although no value is passed, 
        #the POST signal is passed.
        #Confirmed booking, flight database changed

        #Verify that the same ticket can only be booked once
        if request.method == 'POST':
            if flight.capacity > 0:
                flight.book_sum += 1
                flight.capacity -= 1
                flight.income += flight.price
                flight.user.add(request.user)
                flight.save()  #must remember to save
        #Pass the changed ticket information
        context = {
            'flight': flight,
            'username': request.user.username
        }
        return render(request, 'booksystem/book_flight.html', context)


#refund
def refund_ticket(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    flight.book_sum -= 1
    flight.capacity += 1
    flight.income -= flight.price
    flight.user.remove(request.user)
    flight.save()
    return HttpResponseRedirect('/booksystem/user_info')


#sign out
def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'booksystem/login.html', context)


#Log in
def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        user = authenticate(username=username, password=password)
        if user is not None:  #login successful
            if user.is_active:  #Load booking page
                login(request, user)
                context = {
                    'username': request.user.username
                }
                if user.id == ADMIN_ID:
                    context = admin_finance(request)  #Get the data to pass to the front end
                    return render(request, 'booksystem/admin_finance.html', context)
                else:
                    return render(request, 'booksystem/result.html', context)
            else:
                return render(request, 'booksystem/login.html', {'error_message': 'Your account has been disabled'})
        else:  #Login failed
            return render(request, 'booksystem/login.html', {'error_message': 'Invalid login'})
    return render(request, 'booksystem/login.html')


#register
def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                context = {
                    'username': request.user.username
                }
                return render(request, 'booksystem/result.html', context)  #Register successfully and directly render result page
    context = {
        "form": form,
    }
    return render(request, 'booksystem/register.html', context)


#search results page
def result(request):
    if request.method == 'POST':
        form = PassengerInfoForm(request.POST)  #bind data to the form
        if form.is_valid():
            passenger_lcity = form.cleaned_data.get('leave_city')
            passenger_acity = form.cleaned_data.get('arrive_city')
            passenger_ldate = form.cleaned_data.get('leave_date')
            
            #All set to aware comparison
            passenger_ltime = datetime.datetime.combine(passenger_ldate, datetime.time())
            print(passenger_ltime)

            #filter available flights
            all_flights = Flight.objects.filter(leave_city=passenger_lcity, arrive_city=passenger_acity)
            usable_flights = []
            for flight in all_flights:  # off-set aware
                flight.leave_time = flight.leave_time.replace(tzinfo=None)  #The Replace method must be assigned a value. . cry with laughter
                if flight.leave_time.date() == passenger_ltime.date():  #Find only today's flights
                    usable_flights.append(flight)

            # Sort by different keys
            usable_flights_by_ltime = sorted(usable_flights, key=attrgetter('leave_time'))  #Departure time from morning to night
            usable_flights_by_atime = sorted(usable_flights, key=attrgetter('arrive_time'))
            usable_flights_by_price = sorted(usable_flights, key=attrgetter('price'))  #Price from low to high

            # Convert time format
            time_format = '%H:%M'
            
            #Although only one list is converted, in fact all are converted
            for flight in usable_flights_by_price:
                flight.leave_time = flight.leave_time.strftime(time_format)  # converted to str
                flight.arrive_time = flight.arrive_time.strftime(time_format)

            #Determines whether search_head , search_failure are displayed
            dis_search_head = 'block'
            dis_search_failure = 'none'
            if len(usable_flights_by_price) == 0:
                dis_search_head = 'none'
                dis_search_failure = 'block'
            context = {
                #Search multi-frame data
                'leave_city': passenger_lcity,
                'arrive_city': passenger_acity,
                'leave_date': str(passenger_ldate),
                #search results
                'usable_flights_by_ltime': usable_flights_by_ltime,
                'usable_flights_by_atime': usable_flights_by_atime,
                'usable_flights_by_price': usable_flights_by_price,
                #mark
                'dis_search_head': dis_search_head,
                'dis_search_failure': dis_search_failure
            }
            if request.user.is_authenticated:
                print('authenticated')
                context['username'] = request.user.username
            return render(request, 'booksystem/result.html', context)  #If you add /at the front, it becomes the root directory, and the url is wrong.
        else:
            return render(request, 'booksystem/index.html')  #The form submitted on the index interface is invalid and remains in the index interface
    else:
        context = {
            'dis_search_head': 'none',
            'dis_search_failure': 'none'
        }
    return render(request, 'booksystem/result.html', context)
