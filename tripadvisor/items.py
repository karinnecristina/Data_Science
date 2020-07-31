# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TripadvisorItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    autor_comentario = scrapy.Field()
    autor_endereco = scrapy.Field()
    comentario_titulo = scrapy.Field()
    comentario_corpo = scrapy.Field()
    comentario_data = scrapy.Field()
