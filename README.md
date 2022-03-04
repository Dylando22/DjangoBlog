To run blog, first run command in the mysite directory:

python manage.py makemigrations

Then:

python manage.py migrate:

This will set up the database tables for the dynamic data.

Then run:

python manage.py runserver

and go to http://localhost:8000/blog/

