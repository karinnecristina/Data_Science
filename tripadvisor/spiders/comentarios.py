import scrapy
from ..items import TripadvisorItem

class ComentariosSpider(scrapy.Spider):
    name = 'comentarios'
    allowed_domains = ['tripadvisor.com.br']
    start_urls = ['https://www.tripadvisor.com.br/Attraction_Review-g303297-d4037761-Reviews-Lagoa_do_Paraiso-Jericoacoara_Jijoca_de_Jericoacoara_State_of_Ceara.html']

    def parse(self, response):
        item = TripadvisorItem()
        quadro_comentarios = response.xpath("//div[@class='Dq9MAugU T870kzTX LnVzGwUB']")

        for quadro in quadro_comentarios:
            item["autor_comentario"] = quadro.xpath(".//div[@class='_2fxQ4TOx']/span/a/text()").get()
            item["autor_endereco"] = quadro.xpath(".//span[@class='default _3J15flPT small']/text()").get()
            item["comentario_titulo"] = quadro.xpath(".//div[@class='glasR4aX']/a//span/text()").get()
            item["comentario_corpo"] = quadro.xpath(".//div[@class='cPQsENeY']/q/span/text()").get()
            item["comentario_data"] = quadro.xpath(".//span[@class='_34Xs-BQm']/text()").get()
            yield item
        
        next_page = response.xpath("//a[@class='ui_button nav next primary ' and text()='Próximas']/@href").get()
        if next_page:
            yield response.follow(url=next_page, callback=self.parse)




