import unittest
import re
import csv
import redis
from crawler import Crawler

class TestStringMethods(unittest.TestCase):

  def test_filter_product_urls(self):
    foo = Crawler()
    urls = [
      'http://www.epocacosmeticos.com.br/buscapagina/p',
      'http://www.epocacosmeticos.com.br/buscapagina',
      'http://www.epocacosmeticos.com.br/correct/p',
      'http://www.epocacosmeticos.com.br/buscapagina////',
      'http://www.epocacosmeticos.com.br/buscapaginaasdasdasd/p/p/p'
      'http://www.epocacosmeticos.com.br/buscapagina'
    ]
    filtered_urls = foo.filter_product_urls(urls)
    self.assertEqual(filtered_urls, [
      'http://www.epocacosmeticos.com.br/buscapagina/p',
      'http://www.epocacosmeticos.com.br/correct/p'
    ])

  def test_get_links(self):
    foo = Crawler()
    links = foo.get_links('http://www.epocacosmeticos.com.br/')
    self.assertNotEqual(links, [])

  def test_output_csv(self):
    foo = Crawler()
    link_list = [
      'http://www.epocacosmeticos.com.br/buscapagina/p',
      'http://www.epocacosmeticos.com.br/buscapagina',
      'http://www.epocacosmeticos.com.br/buscapagina'
      'http://www.epocacosmeticos.com.br/buscapagina'
    ]
    self.assertTrue(foo.output_csv(link_list, 'test'))

  def test_remove_duplicated_entries(self):
    foo = Crawler()
    link_list_original = [
      'http://www.epocacosmeticos.com.br/buscapagina/p',
      'http://www.epocacosmeticos.com.br/buscapagina1',
      'http://www.epocacosmeticos.com.br/buscapaginalol'
    ]
    link_list_duplicated = [
      'http://www.epocacosmeticos.com.br/buscapagina/p',
      'http://www.epocacosmeticos.com.br/buscapagina/p',
      'http://www.epocacosmeticos.com.br/buscapagina/p',
      'http://www.epocacosmeticos.com.br/buscapagina/p',
      'http://www.epocacosmeticos.com.br/buscapagina/p',
      'http://www.epocacosmeticos.com.br/buscapagina1',
      'http://www.epocacosmeticos.com.br/buscapagina1',
      'http://www.epocacosmeticos.com.br/buscapagina1',
      'http://www.epocacosmeticos.com.br/buscapaginalol'
    ]
    self.assertEqual(sorted(foo.remove_duplicated_entries(link_list_duplicated)), \
      sorted(link_list_original))

  # def test_crawl(self):
  #   foo = Crawler()
  #   foo.crawl('http://www.epocacosmeticos.com.br/)
  #   self.assertTrue(foo.r.lrange('url_list',0,-1))

if __name__ == '__main__':
    unittest.main()