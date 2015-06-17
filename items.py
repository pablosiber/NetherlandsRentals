# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class Website(Item):
	price = scrapy.Field()
	space = scrapy.Field()
	interior = scrapy.Field()
	bedrooms = scrapy.Field()
	description = scrapy.Field()
	agent = scrapy.Field()
	address = scrapy.Field()
	price_inc = scrapy.Field()
	zip_code = scrapy.Field()

