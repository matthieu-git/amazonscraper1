# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# Scraped data -> Item Containers -> Json/csv files
# Scraped data -> Item Containers -> Pipeline -> mySQL

import sqlite3

class AmazonscraperPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()


    def create_connection(self):
        self.conn = sqlite3.connect("amazon_prods.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS prods_tb """)
        self.curr.execute("""create table prods_tb(
                        prod_name text,
                        prod_price_whole int,
                        prod_price_frac int
                        )""")


    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self,item):
        self.curr.execute("""INSERT INTO prods_tb VALUES(?,?,?)""",(
            item['prod_name'][0],
            item['prod_price_whole'][0],
            item['prod_price_frac'][0]
        ))
        self.conn.commit()
