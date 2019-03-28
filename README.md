"# My Taxi project" 

Project outline:
At random times a ride request comes from users.
The request is then broadcast to all drivers.
Whoever picks up first gets to service them.
Assumptions:
1. There are 5 drivers only.
2. All drivers are available at all times
3. A driver can pick up only one request at a time
4. Each request can be picked up by only one driver
5. Whoever picks up the request first gets the ride
6. It takes exactly 1 min to serve each request
7. Every request has 3 states : pending , ongoing,finished
Requirements :
version 1:
1. DRIVER APPS: Built driver web app with 3 TABS : Waiting requests(tab1) , Ongoing
request(tab2), Complete request(tab3).
a. url: /driverapp.html?id=1 or /driverapp.html?id=2 etc... for the 5 drivers
b. Refresh button update statuses
c. Added select buttonnext to ever waiting request .
d. Once select is clickedit is to be verified again that the request is still open
before allotting to a particular driver, since another driver may have picked up in
the meantime.
e. Once a request is picked up, the request status is changed to ongoing and
moved to tab2
f. Once a request is picked up by one driver, remove it from the waiting queue of all
drivers
g. Also after 1 min, the request is automatically set to be finished.
2. CUSTOMER APP: Build a simple form to place new request at any time with customer
a. URL: /customerapp.html
b. Form has 1 textbox for ­ customer id and 1 button to place request
c. Customers can place any number of requests
3. DASHBOARD APP: A simple Web App to show list all requests with request ID ,
time of request, time elapsed and current status(waiting, ongoing) with refresh button

Once a new request is placed, it is shown in the tab1 of all drivers. Whichever driver clicks first
will gets the request and, it will go to their tab2 (say Auto no :3), then it is removed from other
drivers list.

version 2 :
1. Autos are at 5 different locations
a. Auto 1 is always at (1,1)
b. Auto 2 = (2,2)
c. Auto 3 = (3,3)
d. Auto 4 = (4,4)
e. Auto 5 = (5,5)
2. Location also taken when placing requests from customer App
(assume city is a 5km x 5km area )
a. Customer app has textboxes to enter x & y location data: where x,y are
integers from 1 to 5

3. New requests are shown to only 3 nearest available autos in their TAB1.
4. If more than 10 requests are waiting, then reject new requests from CUSTOMER APP
and informs customer with message: “Rides not available. try again later
