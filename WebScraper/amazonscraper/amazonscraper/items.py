# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonscraperItem(scrapy.Item):
    # define the fields for your item here like:

    prod_name = scrapy.Field()
    prod_price_whole = scrapy.Field()
    prod_price_frac = scrapy.Field()
    pass
