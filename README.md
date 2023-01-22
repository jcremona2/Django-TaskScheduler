# Django-TaskScheduler

** This is a sample Django Project to Create Read Update and Delete (CRUD) task on a list **

To install libraries:
```

pip install -r requierments.txt 

```
Django basic commands
```:

python manage.py runserver # Run local server please modify db in settings.py before running

python manage.py makemigrations # Create the steps to create all the tables and models inside the project

python manage.py migrate # Run SQL commands from the 'makemigrations' steps to create the tables in the SQL DB

pytho manage.py shell # interactive shell to work with your project

```

To run it locally the DB settings must be modified, this is intended to work with a postgresql

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


This project was designed to run on a https://dashboard.render.com/ server CI/CD

You can check the project on : https://djangoproject-qsbm.onrender.com 

You can use Render Free to set up your project in a basic server with a posgresdb:

Django docs but you can use almost any other framework:
https://render.com/docs/deploy-django

* Installing poetry is not important as renders tells you, you can use pip to install all the required packages

<img height="30" src="https://github.com/Pythunder/explore/blob/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png">

<img height="30" src="https://github.com/Pythunder/explore/blob/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/django/django.png">

