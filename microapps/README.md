# microapps

---

## Business requirements

- The app should use Pay On API to handle a basic payment transaction to the test bank account. Everything you need can be found in the docs. Also you can take a look at the examples
- All data should be validated. Do not allow to donate more than 100 eur or usd.
Prevent form from submitting multiple times
- Store information about transaction in localstorage (amount, currency, buildNumber, timestamp, ndc, id)
- Same user can donate only 1 time in hour (if user already donated recently, show him a thanks page with donation info, else show form)

## Technical requirements

- It should be a single page application (SPA). In the end you should have one index.html file that includes one .js file and one .css file 
	OK!
- You need to develop the whole app that it could be placed in to AWS S3 bucket and served as a static website. (Ideally you could upload it to your own S3 bucket if you have one or use github pages)
- You can use any front-end framework you like (preferably Angular or React)
	OK!
- Use ES2015 syntax (transpile it with babel)
- Use some css preprocessor like scss or stylus
All logic should be developed using ajax calls to api and localstorage for storing temp data. No database is required.

## Final considerations
#####The candidate must provide:

- A description of the whole process s/he’s followed to come up with this app, along with the decisions s/he’s taken.

---

## How to run:

	npm install
	bower install
	grunt

	http-server build