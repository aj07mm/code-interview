**Setup instructions:**

```
docker-compose up --build
```

to get the authentication token:
```
Request:

POST http://192.168.99.100:8080/auth

{
	"username": "admin",
	"password": "123"
}

Response:

{
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwcmVwX3RpbWUiOiIxIiwibmFtZSI6ImFzZGFzZCIsInZlZ2V0YXJpYW4iOiJUcnVlIiwiZGlmZmljdWx0eSI6IjEifQ.pOgklDEP9qAsUSJsBG-gcoYZ2zRbOnZgoisMJKNMPRc"
}
```

use the given token to make requests to the protected endpoints by adding the following header to them:
```
"Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwicGFzc3dvcmQiOiIxMjMifQ.l9utBfgWGufQdM2z4OPX0h0HrYJ_QPrf1MGOsQ-xwok"
```

- technologies & packages
```
python:3.6
mongo:3.2.3
```
packages:
```
aniso8601==1.3.0
attrs==17.4.0
certifi==2017.11.5
chardet==3.0.4
click==6.7
factory-boy==2.9.2
Faker==0.8.8
idna==2.6
ipaddress==1.0.19
itsdangerous==0.24
MarkupSafe==1.0
marshmallow==2.15.0
mongoengine==0.15.0
nose==1.3.7
pluggy==0.6.0
py==1.5.2
PyJWT==1.5.3
pymongo==3.6.0
pytest==3.3.1
python-dateutil==2.6.1
pytz==2017.3
requests==2.18.4
simplejson==3.13.2
six==1.11.0
text-unidecode==1.1
urllib3==1.22
Werkzeug==0.13
```

I chose python because it is the language I'm more comfortable right now. For the database level I got mongodb because it's easier to start and do operations without the need for a pre defined schema.
For the API I did it with `werkzeug` the main underlying package used in the `Flask` architecture. For mongo connection `pymongo` and orm with `mongoengine`. Serialization with `marshmallow`. Auth with `PyJWT`. Tests with `factory-boy`.

- Search operators

```
e.g.: GET http://192.168.99.100:8080/recipes?name__contains=asdasd
```
2.5.2. Query operators
Operators other than equality may also be used in queries — just attach the operator name to a key with a double-underscore:
```
ne – not equal to
lt – less than
lte – less than or equal to
gt – greater than
gte – greater than or equal to
not – negate a standard check, may be used before other operators (e.g. Q(age__not__mod=5))
in – value is in list (a list of values should be provided)
nin – value is not in list (a list of values should be provided)
mod – value % x == y, where x and y are two provided values
all – every item in list of values provided is in array
size – the size of the array is
exists – value for field exists
```
2.5.2.1. String queries
The following operators are available as shortcuts to querying with regular expressions:
```
exact – string field exactly matches value
iexact – string field exactly matches value (case insensitive)
contains – string field contains value
icontains – string field contains value (case insensitive)
startswith – string field starts with value
istartswith – string field starts with value (case insensitive)
endswith – string field ends with value
iendswith – string field ends with value (case insensitive)
match – performs an $elemMatch so you can match an entire document within an array
```
live on: http://45.55.87.231:8080/
