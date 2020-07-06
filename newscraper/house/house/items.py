# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HouseItem(scrapy.Item):
    Price = scrapy.Field()
    Town = scrapy.Field()
    Area = scrapy.Field()
    Room = scrapy.Field()
    Typeofit = scrapy.Field()
    FloorNumber = scrapy.Field()
    Age = scrapy.Field()
    Heating = scrapy.Field()
    FloorCount = scrapy.Field()
    CreditAvlb = scrapy.Field()
    Furniture = scrapy.Field()
    Firsthand = scrapy.Field()
    MaintenanceFee = scrapy.Field()
    Frontage = scrapy.Field()
    Fuel = scrapy.Field()
    pass
