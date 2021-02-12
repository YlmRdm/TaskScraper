# TaskScraper
TaskScraper is a web scraper for the company that works with Python.

This Repo made with [`Python`](https://www.python.org/) | [`Django`](https://www.djangoproject.com/) | [`Django REST framework`](https://www.django-rest-framework.org/) | [`PostgreSQL`](https://www.postgresql.org/)

This tool tries to scrape some web data from [this website](https://www.koton.com/tr/kadin-suni-kurk-detayli-kaban/p/1KAK06624EW999?productPosition=0&listName=Kad%C4%B1n%20Kaban%20Modelleri#tab-1) to demand.


## Installation

> pip3 install -r requirements.txt

If you just want to see scraping file, Take a look at [`here`]().

## Tasks
You can read [`the task document`](/docs/) to understand better. 
In the meantime, There are some errors in the projects so, this project will be keep going on. 

## Usage

- django-admin startproject taskscraper

- cd taskscraper && python3 manage.py startapp scalprum


## Installed Apps

You should add these inside setttings.py and create a new section called CORS_ORIGIN;

> **<pre>
INSTALLED_APPS = [
    ...
    # Django REST framework 
    'rest_framework',
    'scalprum',
    # CORS
    'corsheaders',
]</pre>**

> **<pre>
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'testdb',
        'USER': 'postgres',
        'PASSWORD': '123',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}</pre>**

> **<pre>
MIDDLEWARE = [
    ...
    # CORS
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]</pre>**

> **<pre>
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
    'http://localhost:8081',
)</pre>**

## Usage(contd.)

- python manage.py makemigrations scalprum

- python manage.py migrate scalprum

- python3 manage.py runserver 8080

<strong><em>NOTE:</strong></em> <strong>You have to install Python >= 3.9 and PostgreSQL >= 13 first.
      Also, you can use pgAdmin4 if you want.</strong>

---
#### Powered by: [`Python`](https://www.python.org/) | [`Django`](https://www.djangoproject.com/) | [`Django REST framework`](https://www.django-rest-framework.org/) | [`PostgreSQL`](https://www.postgresql.org/)