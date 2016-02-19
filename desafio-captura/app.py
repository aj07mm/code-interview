#sitemap-produtos-1.xml & sitemap-produtos-2.xml
#5000 & 2131
#TOTAL: 7131

	# /perfumes
	# /maquiagem
	# /cabelos
	# /dermocosmeticos
	# /tratamentos
	# /corpo-e-banho
	# /beauty-off

from crawler import Crawler
from celery import Celery

BROKER_URL = 'redis://localhost:6379/0'
app = Celery('tasks', broker=BROKER_URL)

@app.task
def do(url):
	foo = Crawler()
	foo.crawl(url)

# do.delay(url="http://www.epocacosmeticos.com.br/")

do.delay(url="http://www.epocacosmeticos.com.br/perfumes")
do.delay(url="http://www.epocacosmeticos.com.br/maquiagem")
do.delay(url="http://www.epocacosmeticos.com.br/cabelos")
do.delay(url="http://www.epocacosmeticos.com.br/dermocosmeticos")
do.delay(url="http://www.epocacosmeticos.com.br/tratamentos")
do.delay(url="http://www.epocacosmeticos.com.br/corpo-e-banho")