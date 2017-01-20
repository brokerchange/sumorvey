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

### Create a superuser
```
python manage.py createsuperuser
```

## Usage
```
python manage.py runserver
```

http://127.0.0.1:8000

