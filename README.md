EconoME is server-side part of EconoME Platform.

Please install docker and docker-compose at your computer.
Then clone this repository(git clone git@github.com:ADA-OOAD-EconoME/EconoME.git) to your computer.
In repository folder create 2 env files: django.env and db_main.env

Mail will not work as we can't expose the mail's passwords, but you can change to your mail server or google server

In the django.env you need store this:
```env
#Django Part

ENVIRONMENT=LOCAL
mail=
password_mail=
backend_email=django.core.mail.backends.smtp.EmailBackend
host_email=


secret_key='Swereirotje8484'

ALLOWED_HOSTS=localhost,0.0.0.0
DEBUG=True

DJANGO_SUPERUSER_PASSWORD=test

#DB
database_user=test
database_name=test_mvp
database_pass=test_pass
database_host=db
database_port=5432

#Redis
REDIS_HOST=redis
REDIS_PORT=6379
REDIS_DB=
REDIS_PASSWORD=

#Flower
FlOWER_USER=
FLOWER_PASSWORD=

#SMS
LSIM_USER=
LSIM_PASSWORD=

#URLS
MAIN=http://localhost/
URL=localhost
PROTOCOL=http
WEB_PROTOCOL=http

#EconoME API
API=http://localhost:8000/api/


#Recaptcha
RECAPTCHA_PUBLIC=
RECAPTCHA_PRIVATE=
```

If you want to turn on debugging mode in django, change in DEBUG False to True

In the db.env you need store this:
```env
POSTGRES_USER=test
POSTGRES_PASSWORD=test_pass
POSTGRES_DB=test_mvp
```

Now, you can run service with help of docker compose.
Type: sudo docker-compose -f docker-compose-db.yml up -d --build

It will build the database.

Then you can run up other services by bash script or docker-compose.

Docker-Compose method:

Type: sudo docker-compose -f docker-compose-main-app.yml up -d --build

Then check all containers, which works.
Type: docker ps
If some container doesn't work, type again: sudo docker-compose -f docker-compose-main-app.yml up -d --build

Now, it must be ok.

Bash method:
First of all you need install python packages. Create virtual environment: python -m venv venv, then activate it: source venv/bin/activate.
Then enter to the folder where requirements.txt and type: pip install -r requirements.txt. Warning!!!: If you are on MacOS delete: uWSGI>=2.0.18,<2.1 in requirements.txt then install packages.

Then create run.sh script and add code:
```bash
#!/bin/bash

set -a
source EconoME/django.env
source venv/bin/activate


cd EconoME/src

python3  manage.py runserver 0.0.0.0:8000

set +a

```
Then change in django.env the database_host to localhost instead of db. Then run the script by typing bash run.sh

For adding superuser account:
Create bash script account.sh and add code:
```bash
#!/bin/bash

set -a
source EconoME/django.env
source env/bin/activate

python EconoME/src/manage.py createsuperuser --no-input  --username=youraccount --email=yourmail@yourmail.com

set +a

```

Run the account.sh script by typing bash account.sh .

Now you can check service in browser on localhost url.

If you made some changes in code, you need type sudo docker-compose -f docker-compose-main-app.yml up -d --build for docker version and anything in python version.
