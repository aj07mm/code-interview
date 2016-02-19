from crawler import Crawler

foo = Crawler()
link_list = foo.filter_product_urls(foo.r.lrange('product_list',0,-1))
foo.output_csv(link_list, 'links')