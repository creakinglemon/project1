# Project 1

Web Programming with Python and JavaScript

DATABASE_URL=postgres://hllfkmecxpxvsh:00ccb6912b1258dffe7674c10403a980e6351dcc574445fd1e8fac6468a9d11b@ec2-3-224-165-85.compute-1.amazonaws.com:5432/dbjo3vq13g5nhl
Goodreads API key: hSJ0g2rNB5V8UliItMyQ5A

Files:
requirements.txt - a list of requirements
application.py - all server-side code
import.py - a python script to read a CSV file and add books from it into a database
books.csv - provided list of books to import into database
createtables.txt - SQL commands required to re-make database
templates - all html/JINJA templates 
static/bootstrap.min.css - bootstrap css file 


The project is complete and fully working:

Database is set up (SQL statements used to re-create database are in createtables.txt), and import.py ccan be run to import books from a CSV file.
The index page displays a list of the top rated books, and a list of most recent reviews.  If either of these is empty, a column of random books is displayed.
Users can register for an account and log in and out.  
Users can search for books by title, author, and/or ISBN (including partials).
All book info is displayed on book page, including info from Goodreads API.
Logged in users can write reviews of books.  
Reviews are displayed on book page.
API is functional.


Things I would improve if I had more time:

Add password hashing.
Error messages are currently handled by rendering a new html page to display the error, and the user has to click the back button to fix the problem.  I would like to handle this by checking input with javascript on the client, and implement message flashing with Flask.
Improve the way the search results are displayed.
Users are always taken back to the index after logging in.  If the user clicked the login link from a book page, I would like to take them back to that page after logging in.
Improve the design of the navbar - both visually, and also to indicate which page is currently active.
Pills on "most recently reviewd" are bigger than "top rated books".
Make the two columns on the homepage wrap on small screens.
Add search box to navbar.
Display the review text in the "most recently reviewed" column on the homepage.