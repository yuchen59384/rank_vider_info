# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
import datetime
class MyprojectPipeline:
    def __init__(self):
        self.date = str(datetime.date.today()).replace('-', '')

    def open_spider(self,spider):
        self.client=pymongo.MongoClient()
    def process_item(self,item,spider):
        myclient=self.client.rank
        mycol=myclient[self.date]
        mycol.insert_one(item)
    def close_spider(self,spider):
        self.client.close()
    # def process_item(self, item, spider):
    #     return item
