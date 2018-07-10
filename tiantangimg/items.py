# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TiantangimgItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    images_name = scrapy.Field()   #图片名字
    images_url = scrapy.Field()   #图片url
