# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonscraperItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = ['https://www.amazon.ca/s?k=avocado&page=2&qid=1574200266&ref=sr_pg_2']

    def parse(self, response):

        items = AmazonscraperItem()

        all_prods = response.css('.s-include-content-margin')

        for avo in all_prods:

            prod_name = avo.css('.widgetId\=search-results > .s-border-bottom .a-color-base.a-text-normal').css('::text').extract()
            prod_price_whole = avo.css('.product-list__listview-price::text').extract()
            prod_price_frac = avo.css('.product-list__listview-price::text').extract()

            items['prod_name'] = prod_name
            items['prod_price_whole'] = prod_price_whole
            items['prod_price_frac'] = prod_price_frac

            yield items