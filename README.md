# Graveyard: Place for Dead (and Undead)

Graveyard is an attempt at open-source reimplementation of DraciDoupe.cz (referred to as DDCZ in this text).

Developer's documentation is [at Read the Docs](https://ddcz.readthedocs.io/en/latest/). 

## Installation

You can run Graveyard either directly on your machine or inside [Docker](https://www.docker.com/).

Installing and running Graveyard directly is faster (on some systems) and removes one lever of indirection, but it makes the setup more compliated. 

Running in Docker requires familiarity with it, but it makes setup easier and guarantees consistency with the testing environment (and hopefully in the future, production environment as well). 

In both cases, first clone this repository and run all commands in it. 

### Installing in Docker

Requirements:

* You have [Docker CE installed](https://www.docker.com/community-edition)
* You have [installed docker-compose](https://docs.docker.com/compose/install/)

Verify you have everything ready by running the test suite:

* `docker-compose run web python3 manage.py test`

If you see output like this:

```
(graveyard-venv) almad@zeruel:~/projects/graveyard$ docker-compose run web python3 manage.py test
Starting graveyard_db_1 ... done
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
....
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
Destroying test database for alias 'default'...
(graveyard-venv) almad@zeruel:~/projects/graveyard$ 

```

You are all set. Afterwards, install database schema by running

*  `docker-compose run web python3 manage.py migrate`

You are done! Now you can just run the project and develop using

*  `docker-compose start`


### Installing on your machine

Graveyard is currently written in [Django](https://www.djangoproject.com/). Requirements to develop it:

* You have working Python 3 installation on your machine
* You have working MySQL installation on your machine

To use the project, clone this repository and:

* Create a virtual environment: `python3 -m venv gvenv`
* Enter it (on Mac OS X or Linux): `source gvenv/bin/activte`
* Copy settings template: `cp graveyard/settings/local.example.py graveyard/settings/local.py`
* Edit the settings above, especially enter credentials to your local MySQL
* Create the database schema: `python manage.py migrate`
* Run the thing! `python manage.py runserver`
* Observe if you have contact at `http://localhost:8000`
* Maybe create a superuser in order to enter admin: `python manage.py createsuperuser`
* Look around the administration interface at `http://localhost:8000/admin/`


