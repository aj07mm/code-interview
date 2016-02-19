# desafio-captura - prova para entrar na Sieve
A crawler that visits the site 'epocacosmeticos.com.br' and generates a links.csv file with a list of product links.

#HOW TO RUN:

	$ pip install -r requirements.txt
	#If you don't have redis:
		#Linux:
			$ apt-get install redis-server
			$ export C_FORCE_ROOT="true"
	    #Mac:
			$ brew install redis
	$ celery -A app worker --loglevel=info
The crawler stays crawling in a recursive way doing parallel processing, so if you want to output the current crawled results, do the following to generate the file:

	$ python output.py