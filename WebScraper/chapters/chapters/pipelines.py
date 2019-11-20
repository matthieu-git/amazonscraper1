# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import mysql.connector


class ChaptersPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            passwd = 'Dfg19682!',
            database = 'myavocados'
        )
        self.curr = self.conn.cursor()

    def create_table(self):

        self.curr.execute("""DROP TABLE IF EXISTS cprods_tb """)
        self.curr.execute("""create table cprods_tb(
                        prod_name text,
                        prod_price text
                        )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""insert into cprods_tb values (%s,%s)""", (
            item['prod_name'][0],
            item['prod_price'][0]
        ))
        self.conn.commit()



