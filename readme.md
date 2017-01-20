# Sumourvey

A responsive Django app to display, record and provide results of survey questions presented to users.

## Built With

* [Django](http://www.djangoproject.com/) 
* [mysqlclient](https://github.com/PyMySQL/mysqlclient-python)
* [django-flat-responsive](https://github.com/elky/django-flat-responsive) - responsive fix for Django Admin
* [django-bootstrap-themes](https://github.com/no-dice/django-bootstrap-themes) - Bootstrap themes

## Prerequisites

Python 3.6 (though 3.x should work)

Pip

MySQL (developed against 5.7.17)

## Installing

### Clone this repo
```
git clone https://github.com/sqweak/sumorvey.git
```

### Install requirements.txt with pip
```
pip install -c requirements.txt
```
### Initialize db
Creates the database and user/permissions expected by django. 
```
mysql < init_db.sql
```
Alternatively, edit db info in *survsite/settings.py* 

### Perform initial migrate

```
python manage.py migrate
```
### Populate data

```
python manage.py loaddata seed
```

### Create a superuser
```
python manage.py createsuperuser
```

## Usage
```
python manage.py runserver
```

Launch the app at http://127.0.0.1:8000

1. Answer questions. 
2. ???
3. Profit!

## Admin

Login to http://127.0.0.1:8000/admin/ with the superuser credentials you created

### Add questions

On the admin dashboard, click Add.

(Optional) Choose a prerequisite answer. If a prereq is selected, this quesiton will only be shown to users who have selected that answer.

Enter the question in the Text field.

Enter answers in the Text fields below. Add more fields as needed.

## Admin use of the app

After logging in to admin panel, visits to the app will have a navbar in the header.

### Results

Clicking results will show a table of all questions and answers with vote totals. Click a question name to see more info!

### Purge Session

Sumorvey uses sessions to track questions answered (to avoid repeats) and answers selected (to qualify users for questions containing a prerequisite). Click this link to reset the session.

### Purge Results

Click this link to clear all votes in the database.




