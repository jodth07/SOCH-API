# SOCH Back End API (Python & Django REST)

A django-rest api for Sisters of Culture Hair project

## Features

- It uses the latest python version (as of Oct 2018).
- Ready to deploy to heroku in just 1 minute (for free).
- 100% compatible with [c9.io](http://c9.io) .

## How to install this project :question:

Follow these steps:

Make sure you have python 3.6 installed, if you are using Cloud9 you can install it by typing:
```
$ pyenv install 3.6.6   (this step takes a while)

$ pyenv global 3.6.6
```


##### Clone this project - BackEnd from :
```
$ git clone https://github.com/jodth07/SOCH-API.git
$ pipenv install
$ pipenv shell
```

Run migrations
```
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser
```

Start the python server

```
$ python manage.py runserver $IP:$PORT (on c9)
$ python manage.py runserver 
```


## What next?

Your python API should be running smoothly on port 8000

###set up the front end from 
`https://github.com/jodth07/SOCH-FE`

add images, products, styles and users.
(make sure to change and update paypal info)


## Deploy your project to Heroku
If you don't have your code connected to a github repository, please do it:
```
$ git init
$ git add -A
$ git commit -m "Initial commit"
```
Then, run these 3 steps to deploy to heroku:
```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
```

### Aditional Tutorials
- [Working with django /admin](https://github.com/4GeeksAcademy/django-rest-hello/blob/master/docs/ADMIN.md) to create superusers, add models to your admin, etc.
- [Using the python shell](https://github.com/4GeeksAcademy/django-rest-hello/blob/master/docs/DATABASE_API.md) to CRUD models, etc.
- [Working with Migrations](https://github.com/4GeeksAcademy/django-rest-hello/blob/master/docs/MIGRATIONS.md) for everytime you change your model
- [Using MySQL](https://github.com/4GeeksAcademy/django-rest-hello/blob/master/docs/MYSQL.md) insalling and using MySQL in your application.
- [Using Mongo](https://github.com/4GeeksAcademy/django-rest-hello/blob/master/docs/MONGO.md) insalling and using mongo in your application.

## Packages Being Used (Documentation)
- [Django CORS Headers](https://github.com/ottoyiu/django-cors-headers)
- [Django REST Framework](https://github.com/encode/django-rest-framework)
