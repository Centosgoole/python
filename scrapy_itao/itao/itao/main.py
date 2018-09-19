from scrapy import cmdline
cmdline.execute('scrapy crawl itao_spider -o info.csv -t csv'.split())