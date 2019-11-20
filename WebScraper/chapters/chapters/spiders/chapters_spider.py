# -*- coding: utf-8 -*-
import scrapy
from ..items import ChaptersScraperItem

class ChaptersSpiderSpider(scrapy.Spider):
    name = 'chapters_spider'
    start_urls = ['https://www.chapters.indigo.ca/en-ca/home/search/?keywords=avocado#internal=1']

    def parse(self, response):
        items = ChaptersScraperItem()

        all_prods = response.css('.product-list__product-container')

        for avo in all_prods:

            prod_name = avo.css('.product-list__product-title-link--grid::text').extract()
            prod_price = avo.css('.product-list__listview-price::text').extract()

            items['prod_name'] = prod_name
            items['prod_price'] = prod_price

            yield items

# prod_name = response.css('.product-list__product-title-link--grid::text').extract()
# prod_price = response.css('.product-list__listview-price::text').extract()