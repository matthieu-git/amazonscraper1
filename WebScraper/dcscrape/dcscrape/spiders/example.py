# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess


class IndependentScraper( scrapy.Spider ):
    name = 'independent'

    def start_requests(self):
        urls = ['https://www.walmart.ca/search/avocado/page-1']
        for url in urls:
            yield scrapy.Request( url = url, callback = self.parse)

    def parse(self, response):
        # simple example: write out the html
        html_file = 'independent.html'
        with open( html_file, 'wb' ) as fout:
            fout.write( response.body )

# initiate a CrawlerProcess
process = CrawlerProcess()

# tell the process which spider to use
process.crawl(IndependentScraper)

# start the crawling process
process.start()