Goodreads - Your Online Library 📚

Welcome to Goodreads, an innovative platform where students can read books online, share their thoughts, and engage with fellow readers! 📖

This project aims to create an online library where users can:

Read books online 📕
Stream and access a wide range of books from various genres
Share and discuss favorite books with friends and fellow students
Like, comment, and rate books to help others find great reads
Build a personal library of favorite titles


Tech Stack 🔧

Backend: Django
Database: PostgreSQL
Asynchronous Task Queue: Celery with RabbitMQ
Message Broker: RabbitMQ
Email Notifications: Celery tasks for email sending

How to Set Up and Run Locally 🖥️

To get this project running on your local machine, follow these simple steps:

Prerequisites
Before starting, ensure you have the following installed:

Python 3.8+
Django 3.x (or the version specified in requirements.txt)
PostgreSQL (for managing the database)
RabbitMQ (for managing background tasks)


Steps to Set Up
Clone the repository
First, clone the repository to your local machine:
git clone https://github.com/Muhammadaziz-dev/goodreads.git
cd goodreads


Create a virtual environment and install dependencies
Set up a Python virtual environment and install the required dependencies:
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt

Set up the PostgreSQL database
Create a new PostgreSQL database for the project:
CREATE DATABASE goodreads;
Then, update your settings.py file to configure the PostgreSQL database credentials:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'goodreads',
        'USER': 'your-db-username',
        'PASSWORD': 'your-db-password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

Set up RabbitMQ
RabbitMQ is used for handling background tasks. If you haven't installed it yet, follow the RabbitMQ installation guide.
Start RabbitMQ:
sudo systemctl start rabbitmq-server

Run migrations
Apply the database migrations to set up the schema:
python manage.py migrate

Start the Django development server
Launch the development server to view the app locally:
python manage.py runserver
Now, you can access the app at http://127.0.0.1:8000/ in your browser.


Start Celery to handle background tasks (email sending)
Open a new terminal window and start the Celery worker process:
celery -A goodreads worker --loglevel=info
(Optional) Run the Celery Beat scheduler

If you have periodic tasks (e.g., daily notifications), you can run the Celery Beat scheduler:
celery -A goodreads beat --loglevel=info

and run the
python manage.py test
command
