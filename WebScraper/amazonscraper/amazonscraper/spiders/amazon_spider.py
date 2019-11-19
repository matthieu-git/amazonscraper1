# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonscraperItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = ['https://www.amazon.ca/s?k=avocado&qid=1574118995&ref=sr_pg_1']

    def parse(self, response):
        items = AmazonscraperItem()

        prod_name = response.css('.widgetId\=search-results > .s-border-bottom .a-color-base.a-text-normal').css('::text').extract()
        prod_price_whole = response.css('.a-price-whole::text').extract()
        prod_price_frac = response.css('.a-price-fraction::text').extract()

        items['prod_name'] = prod_name
        items['prod_price_whole'] = prod_price_whole
        items['prod_price_frac'] = prod_price_frac

        yield items