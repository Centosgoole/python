# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MinglujiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #公司名称
    Company_Name = scrapy.Field()
    #国家
    Country = scrapy.Field()
    #地址
    Address = scrapy.Field()
    #手机
    Phone = scrapy.Field()
    #email
    Email = scrapy.Field()
    #web_url
    web_url = scrapy.Field()
    #分类
    Category = scrapy.Field()
    #单个url
    get_url = scrapy.Field()