# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import code
import scrapy

class AnimeItem(scrapy.Item):
    title = scrapy.Field()
    code = scrapy.Field()
    edition = scrapy.Field()
    pass
