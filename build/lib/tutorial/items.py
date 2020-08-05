# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    jobname = scrapy.Field()
    country = scrapy.Field()
    city = scrapy.Field()
    productname = scrapy.Field()
    categoryname = scrapy.Field()
    responsibility = scrapy.Field()
    updatetime = scrapy.Field()


class DoubanItem(scrapy.Item):
    username = scrapy.Field()
    comment = scrapy.Field()
    updatetime = scrapy.Field()


class SunItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
    detail = scrapy.Field()
    status = scrapy.Field()
