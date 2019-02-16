"# mytaxi_backend" 
Based on Django framework with MYSQL database
Two main modules:-
1) taxi_auth-- implemented without authentication, has basic user model, role model that conatins user-role-mapping. A user view for adding/removing user. Roles are- driver, customer and admin  
2) taxi-ride:- contains request model and APIs to request, accept and complete a ride. It also contains dashboard APIs for driver and admin    
To be done:- Fix issue for foreign keys (can be fixed after implementing basic auth) , complete ride after 5 minutes even if the user closes the frontend through a cron   
 
