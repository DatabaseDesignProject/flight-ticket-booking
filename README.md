[Detailed Introduction -Database Course Design -Air Ticket Reservation System -Short Book](http://www.jianshu.com/p/60a392df9f03)

Both the registration and login interface learn from this man's [buckyroberts-Viberr](https://github.com/buckyroberts/Viberr)

## Five, interface design

### 5.1 Welcome screen

![Welcome interface](http://upload-images.jianshu.io/upload_images/1877813-c078119ecf8b22bf.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

Plan a trip (Changsha→Shanghai 2017/4/2)

![input itinerary](http://upload-images.jianshu.io/upload_images/1877813-8e7d67d4ba9be92c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 5.2 Query interface
After the user Let's Go, load the query results page.
![Successful query interface](http://upload images.jianshu.io/upload images/1877813 c607acdbf2f65b32.png?image mogr2/auto orient/strip%7 cimage view2/2/w/1240) 

The default ticket information is based on the price In ascending order, the user can choose to sort in ascending order by departure time or arrival time by clicking the field above the ticket information, as shown in the figure below, pay attention to the changes in the last two lines.

![The query results are sorted in ascending order of departure time](http://upload images.jianshu.io/upload images/1877813 59e9c048ac02d75b.png?image mogr2/auto orient/strip%7 cimage view2/2/w/1240) 

If the user / If the required flight database does not exist, an error message will be returned.
Modify the user's destination to China (there is no such flight in the database) for testing.
![查询失败界面](http://upload-images.jianshu.io/upload_images/1877813-b01972455fe041a1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 5.3 Ticket booking interface
![Click the booking button to book a ticket](http://upload-images.jianshu.io/upload_images/1877813-f31476f891dae2ff.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

Since the user has not logged in, it will be directly fed back to the login interface.


![Login page](http://upload-images.jianshu.io/upload_images/1877813-19d3851f0df7eb48.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

Since the user has not yet registered, the user clicks Click here on this page to enter the account registration page to complete the account registration.

![Registration page](http://upload images.jianshu.io/upload images/1877813 78e026c005cb9b8e.png?image mogr2/auto orient/strip%7 cimage view2/2/w/1240) After the user registers, the account is directly loaded into query page. 

![After successful login](http://upload images.jianshu.io/upload images/1877813 1ce7b06008a254f7.png?image mogr2/auto orient/strip%7 cimage view2/2/w/1240) The user clicks to book again, If the user has not booked the flight, load the booking confirmation page, if the user has already booked, load the booking conflict page. 

![Normal booking page](http://upload images.jianshu.io/upload images/1877813 84ddfba39dca9100.png?image mogr2/auto orient/strip%7 cimage view2/2/w/1240) On the normal booking page Click Confirm to complete the booking.

![Complete the booking on the normal booking page](http://upload-images.jianshu.io/upload_images/1877813-d0cac0d501cfb050.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

In the personal center, users can view their own booking information.


![User Personal Center](http://upload-images.jianshu.io/upload_images/1877813-070977fbe83f6167.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

If the user selects a ticket that he has already booked, load the booking conflict page.


![booking conflict page](http://upload-images.jianshu.io/upload_images/1877813-9c2f7a2ece954b5f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 5.4 Refund interface

In the user's personal center, you can refund the ticket.
![Refund page](http://upload-images.jianshu.io/upload_images/1877813-010c33405c8e8794.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

Select Confirm to complete the refund and refresh the user's booking information.


![User's personal center after refund](http://upload-images.jianshu.io/upload_images/1877813-ef2d63e1012518d3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 5.5 Admin UI

![Administrator admin login account](http://upload-images.jianshu.io/upload_images/1877813-bfe34ac3da390ca0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

In the previous login_user function, it has been determined that if the login user is an administrator, load the airline's financial page.
![Login_user function login user identity determination](http://upload-images.jianshu.io/upload_images/1877813-b62cc6784cd273f9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

The administrator login is successful.
![Admin Page -Company Financial Information](http://upload-images.jianshu.io/upload_images/1877813-cc4afc25d37c4ef9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 5.6 Background management interface

Enter admin at the end of the link to enter the background management


![Enter background](http://upload-images.jianshu.io/upload_images/1877813-5b533403b65c584e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

Administrator login account


![Admin login](http://upload-images.jianshu.io/upload_images/1877813-d2bfaf67531e5d9b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

Background data, including Flight, User, and Django's default-generated data.
![Background interface](http://upload-images.jianshu.io/upload_images/1877813-5d97aa787c87e85d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

Flight information management, display all flight information, you can add, delete, modify and check.

![Flight information management](http://upload-images.jianshu.io/upload_images/1877813-14106ac6b678c1df.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

Passenger information management, operation is the same as flight information management, and the information of registered users will be saved here.

![Passenger Information Management](http://upload-images.jianshu.io/upload_images/1877813-0d2f61b05e1b9393.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
