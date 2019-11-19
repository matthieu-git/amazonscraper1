# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess


class WalmartSpider( scrapy.Spider ):
    name = 'walmart'

    def start_requests(self):
        urls = ['https://www.walmart.ca/search/avocado/page-1']
        for url in urls:
            yield scrapy.Request( url = url, callback = self.parse)

    def parse(self, response):
        links = response.css('h2.thumb-header::text').extract()
        filepath = 'walmart_prods.csv'
        with open( filepath, 'w' )as f:
            f.writelines( [link + 'n' for link in links] )

# initiate a CrawlerProcess
process = CrawlerProcess()

# tell the process which spider to use
process.crawl(WalmartSpider)

# start the crawling process
process.start()