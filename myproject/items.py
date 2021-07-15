# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyprojectItem(scrapy.Item):
    # define the fields for your item here like:
    _id = scrapy.Field()
    tag=scrapy.Field()
    play = scrapy.Field()
    dm = scrapy.Field()
    title= scrapy.Field()
    dz= scrapy.Field()
    tb= scrapy.Field()
    author=scrapy.Field()
    sc= scrapy.Field()
    fx= scrapy.Field()
    href=scrapy.Field()
    pass

