# Onyo
## Backend Challenge

## Description:

- We have two RESTful apis: `/ana` and `/bob`
- Both have the endpoint `/address`.
- Both of them communicate with each other by JSON.

- `/ana/address` receives all CRUD operations and `/bob/address` too, but on POST requests she calls `/bob/address` first and then save the response on the database.
- `/bob/address` when receives calls, it concatenates a random float number ranging from 0 to 1, to the string value of each field in the JSON object. Then, saves it on the database and sends this as a response to the caller.

e.g.

	POST /bob/address

	request:

		{
			"country": "brasil",
			"state": "rio de janeiro",
			"city": "niteroi"
		}

	response:

		{
			"id": 1,
			"country": "brasil0.123123123",
			"state": "rio de janeiro0.123123123",
			"city": "niteroi0.123123123"
		}

__Note:__0.123123123 is a random number


## Requirements:

- create two APIs (OK!)
- communicate with each other by JSONs (OK!)
- keep their databases separated (OK!)
- Both of them should answer to simple CRUD requests
	- Bob (OK!)
	- Ana (OK!)
- We'll have two APIs (Ana and Bob) (OK!)
- having a POST to Ana, Ana should perform a request to Bob and will save the answer of Bob on its own database (OK!)
- Bob should have API calls to return random values when its created, so when we have the same input coming from Ana we should have the same answer from Bob (OK!)
- Bob will have to store some data on its own database (OK!)

- Refactor (OK!)

- Unit tests (OK! almost...)

- Integrations tests (OK! almost...)

- PR

- Deploy (OK!)

- needed decoupling between them (OK! The only place you have to change on ana to adapt for evetual changes on bob is the model, because it saves on the database with the corresponding fields.)

---

### How to run api:

	$ virtualenv onyo
	$ source onyo/bin/activate

	$ pip install -r requirements.txt

	$ python manage.py migrate
	$ python manage.py migrate --database=ana_db
	$ python manage.py migrate --database=bob_db

	$ python manage.py loaddata initial_data.json

	$ python manage.py runserver 0.0.0.0:8000

---

### How to run test:

	$ python manage.py runserver 0.0.0.0:8000
	$ python manage.py test

__Note:__ Integration tests assuming bob is running on localhost:8000, to change the path go to `api/settings.py and change the `EXTERNAL_URLS['bob']` variable.

---

### Demo:

- [http://104.131.106.176:8000/ana/](http://104.131.106.176:8000/ana/)
- [http://104.131.106.176:8000/bob/](http://104.131.106.176:8000/bob/)

######Credentials:

		username: root
		password: root

---

### Project Description:

The main goal of this challenge is to exercise some concepts of API Rest, microservices and integrations. The basic goal is to create two APIs (microservices) using Django Rest Framework or similar web frameworks. These microservices should communicate with each other by JSONs, but should keep their databases separated. Both of them should answer to simple CRUD requests -- Get, Post, Put, Delete. We'll have two APIs, let's consider the first API "Ana" and the second one "Bob". When having a POST to Ana, Ana should perform a request to Bob and will save the answer of Bob on its own database. Bob should have API calls to return random values when its created, so when we have the same input coming from Ana we should have the same answer from Bob. In order to do it, Bob will have to store some data on its own database. The main reason is the needed decoupling between them.

The models, views and business rules may be created at your own criteria. We're interested on the dynamics that these parts will connect to each other.

As a topic we have a few suggestion:

Bob could serve Postal Code Information (Street, City, State, etc) given a Postal Code it will return information. Ana should consume Bob and propagate its answer.

Bob could be serving Lotto Check Service. Given 6 number, Bob will tell Ana if its a winner combination or not. Ana should cache its answer in order to avoid calling Bob many times.

Fell free to follow any topic, but please make sure you have understood the purpose of its challenge.

Must have

Unit tests
Integrations tests
Documentation
Deployment (Heroku, Openshift, DigitalOcean)
Clean, readable, maintainable, and extensible code
Decoupling on two different folders
Optional, but recommended

Django Rest Framework
Interface
ATENTION

Don't worry about the topic you'll chose to work on. Fell free to work on a confortable topic.
You should not try to push changes directly to this repository.
Submission Process

The candidate must implement the APIs and send a Pull Request to this repository with the solution.

The Pull request process works this way:

The candidate forks the repository (should not clone it directly)
Works on the code using the forked repository.
Commits and push changes to the forked repository.
Using the GitHub interface, send the pull request.st.