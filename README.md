# Issue Tracker System
 - Web app that manage the tickets for users

## TABLE OF CONTENT
   - Introduction
   - Project Structure
   - Project source
   - Project Overview
   - Database
   - Usage
   - Description pages
   - Description of functions in python
   - Technology Used

## INTRODUCTION
- This web app manages not only to manage the requests that are made by users, but also keeps track of the list of all the
issues that are made by users. The user first of all has to do the free registration to get the basic services, moreover he
can also extend the request of the services according to the packages that are exposed on the home page.

## PROJECT STRUCTURE
![screenshot 4](static/img/Structure.jpg?raw=true "Structure")

## PROJECT SOURCE
Project source can be download from the following link:
https://github.com/zainshafiq2017/issuetracker.git

## Issue Tracker System  (SCREENSHOT)
![screenshot 1](static/img/index.jpg?raw=true "index")
![screenshot 2](static/img/profile.jpg?raw=true "profile")
![screenshot 3](static/img/new_ticket.jpg?raw=true "new tickets")
![screenshot 3](static/img/ticket.jpg?raw=true "ticket")
![screenshot 3](static/img/stripe.jpg?raw=true "stripe orders")
![screenshot 3](static/img/charts.jpg?raw=true "charts")

## PROJECT OVERVIEW
### WHAT PROBLEM THIS WEBSITE SOLVE?
 - This webapp allows to solve many technical problems that companies face every day for their projects.

### PROJECT OBJECTIVE
 - The main goal is to create a fairly simple and complete platform for companies and ICT helpdesk.

### HOW DOES IT WORK
 - The user must make a ticket through the form and then he will be contacted by helpdesk.

## DATABASE
 - In the local environment the database used is DB sqlite, while in the server environment it's postgres DB.

## USAGE
### QUICK START
Open your command line and use:
git clone https://github.com/zainshafiq2017/issuetracker.git
cd issue-tracker
virtualenv env
source env/bin/activate
Install the dependencies:
```cmd
pip install -r requirements.txt.
```

Run the development server

Open your browser and navigate to http://127.0.0.1:5000

To import data to MongoDB is the following command:
mongoimport -d donorsUSA -c projects --type csv --file opendata_projects_clean.csv --headerline

### DEPLOYING TO HEROKU
 - Signup for Heroku
 - Login to Heroku and download the Heroku Toolbelt
 - Once installed, open command line and run the following command `heroku login` and follow prompts.
 - Activate your virtualenv
 - All dependencies have to be added to a requirements.txt with `pip freeze > requirements.txt` command.
 - Create a -procfile with editor and save it with the following text `web: gunicorn donations_Nebraska:app` that tells what to do with application once it's been deployed
 - Create a local Git repository:
   ```cmd
   git init
   git add .
   git commit -m "initial files"
   ```
 - Create your app on Heroku:
   `heroku create <git-url-for-your-app>`
 - Deploy your code to Heroku:
   `git push heroku master`
 - View your app on browser:
   `heroku open`

### Useful Command lines
 - django project
 - django-admin startproject name_project
 - django-admin startapp todo (create app)
 - python3 manage.py makemigrations
 - python3 manage.py migrate
 - python3 manage.py test (To test code)
 - python3 manage.py createsuperuser

## Description pages
** Profile page **
 - In the profile page single user can see the list of his requested tickets. Furthermore, user can also see the progress made
on ticket if it is to do, in progress or done. The problem resolution is also explained so that there is clear transparency.
The page also contains the total of orders placed by a single user.

** Tickets **
 - The new ticket page allow users to create a new ticket when they encounter the technical problems. Simply filling the form
that is presented in the appropriate page later by pressing the save button.

 - In Ticketlist page users view all requests made by all users so in this way everyone can read all tickets in detail.

** Charts **
- In the chart page I show for each title the total of the views. The chart makes the idea of more or less how active is the site.

** Cart **
 - Temporary orders are added to the cart page, which can be deleted or sent forward for checkout, where the form will be 
displayed to populate data for purchase orders. 

## DESCRIPTION OF FUNCTIONS IN PYTHON
### ticket (views.py)
 - Piece of code:
   ```
   def get_tickets(request):
   """
   Create a view that will return a list
   of tickets that were entered and render
   them to the 'request_ticket.html'
   """
    
   tickets = Ticket.objects.filter(reported_on__lte=timezone.now()).order_by('-reported_on')
   return render(request, "request_ticket.html", {'tickets':tickets})
   ```
### packages (views.py)
 - Piece of code:
   ```
   def all_packages(request):
   packages=Package.objects.all()
   return render(request, "packages.html", {"packages":packages})
   ```
### charts (views.py)
 - Piece of code:
   ```
   def get_data(request):
   """
   Sending all ticket in json format to api/data/
   """
   
   ticket = Ticket.objects.all()
   return HttpResponse(serializers.serialize('json', list(ticket)), content_type="application/json")
   ```

## TECHNOLOGY USED
 - [Bootstrap](https://getbootstrap.com/docs/4.0/getting-started/introduction/)
 - [Django](https://www.djangoproject.com/)
   Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
 - [Charts JS](http://www.chartjs.org/)
   Mix and match bar, line and other charts to provide a clear visual distinction between datasets.
 - [PostgreSQL](https://www.postgresql.org/?&)
 - [Sqlite](https://www.sqlite.org/index.html)
 - jquery
 - queue
 - python
 - javascript
 - HTML
 - CSS

## Supported browsers
 - I've used Mozilla browser on creating this web app. Mobile browsers should support all styles and screen size.

## FILE LOCATIONS
 - Static files such as CSS, Javascript and images can be found in the static subdirectory.
 - Templates can be found in the templates subdirectory.