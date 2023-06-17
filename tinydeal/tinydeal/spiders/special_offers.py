import scrapy


class SpecialOffersSpider(scrapy.Spider):
    name = "special_offers"
    allowed_domains = ["web.archive.org"]
    start_urls = ["https://web.archive.org/web/20190225123327/https://www.tinydeal.com/specials.html"]

    def parse(self, response):
        for product in response.xpath("//ul[@class='productlisting-ul']//li"):
            yield{
                "title":response.xpath(".//a[@class='p_box_title']/text()").get(),
                "url":response.urljoin(response.xpath(".//a[@class='p_box_title']/@href").get()),
                "discounted_price":response.xpath(".//span[@class='productSpecialPrice fl']/text()").get(),
                "original_price":response.xpath(".//span[@class='normalprice fl']/text()").get(),
                "image":response.urljoin(response.xpath(".//a[@class='p_box_img']/img/@src").get())
            }
