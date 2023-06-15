import scrapy


class CountriesSpider(scrapy.Spider):
    name = "countries"
    allowed_domains = ["www.worldometers.info"]
    start_urls = ["https://www.worldometers.info/world-population/population-by-country"]

    def parse(self, response):
        countries = response.xpath("//table[@id='example2']//td[2]/a")
        for country in countries:
            name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()

            #yield scrapy.Request(url=f"https://www.worldometers.info{link}")
            #yield scrapy.Request(url=response.urljoin(link))
            yield response.follow(url=link)