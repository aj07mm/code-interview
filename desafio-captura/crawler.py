import mechanize
import re
import csv
import redis
import sys

class Crawler:
    def __init__(self):
        self.r = redis.StrictRedis(host='localhost', port=6379, db=0)
        '''visited links'''
        self.loop = 0

    def get_links(self, url):
        url_list = []
        br = mechanize.Browser(factory=mechanize.RobustFactory())
        br.open(url)
        for link in br.links(url_regex='http://www.epocacosmeticos.com.br/(.*)'):
            url_list.append(link.url)

        return url_list

    def crawl(self, url):
        self.loop = self.loop + 1
        links = self.get_links(url)
        for link in self.filter_product_urls(links):
            self.r.lpush('product_list', link)
        self.r.lpush('url_list', url)
        url_list = self.r.lrange('url_list',0,-1)

        print self.loop

        for link in links:
            if link not in url_list:
                self.crawl(link)

    def filter_product_urls(self, links):
        pattern = 'http://www.epocacosmeticos.com.br/[a-zA-Z0-9-]*/p$'
        r = re.compile(pattern, re.MULTILINE)
        return filter(r.match, self.remove_duplicated_entries(links))

    def remove_duplicated_entries(self, links):
        return list(set(links))

    def output_csv(self, link_list, filename):
        try:
            with open(filename+'.csv', 'wb') as f:
                writer = csv.writer(f)
                for val in link_list:
                    writer.writerow([val])
            return True
        except IOError:
            return False
