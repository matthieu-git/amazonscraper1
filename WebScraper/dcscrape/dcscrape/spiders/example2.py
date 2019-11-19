# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess


class DCspider( scrapy.Spider ):
    name = 'dc_spider'

    def start_requests(self):
        urls = ['https://www.datacamp.com/courses/all']
        for url in urls:
            yield scrapy.Request( url = url, callback = self.parse)

    def parse(self, response):
        links = response.css('div.course-block > a::attr(href)').extract()
        filepath = 'DC_links.csv'
        with open( filepath, 'w' )as f:
            f.writelines( [link + 'n' for link in links] )

# initiate a CrawlerProcess
process = CrawlerProcess()

# tell the process which spider to use
process.crawl(DCspider)

# start the crawling process
process.start()