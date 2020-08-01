import scrapy
from ..items import TripadvisorItem


class ComentariosSpider(scrapy.Spider):
    name = 'comentarios'
    allowed_domains = ['tripadvisor.com.br']
    start_urls = ['https://www.tripadvisor.com.br/Attraction_Review-g303297-d4037761-Reviews-Lagoa_do_Paraiso-Jericoacoara_Jijoca_de_Jericoacoara_State_of_Ceara.html#REVIEWS']

    def parse(self, response):
        item = TripadvisorItem()
        frames = response.xpath("//div[@class='Dq9MAugU T870kzTX LnVzGwUB']")
        for item_frames in frames:
            item["author"] = item_frames.xpath(".//a[@class='ui_header_link _1r_My98y']/text()").get()
            item["address"] = item_frames.xpath(".//span[@class='default _3J15flPT small']/text()").get()
            item["title"] = item_frames.xpath(".//div[@class='glasR4aX']/a//span/text()").get()
            item["comment"] = item_frames.xpath(".//q[@class='IRsGHoPm']/span/text()").get()
            item["date"] = item_frames.xpath(".//span[@class='_34Xs-BQm']/text()").get()
            yield item
        
        next_page = response.xpath("//a[@class='ui_button nav next primary ' and text()='Próximas']/@href").get()
        if next_page:
           yield response.follow(url=next_page, callback=self.parse)