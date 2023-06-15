import scrapy


class GdpDebtSpider(scrapy.Spider):
    name = "gdp_debt"
    allowed_domains = ["worldpopulationreview.com"]
    start_urls = ["https://worldpopulationreview.com/country-rankings/countries-by-national-debt"]

    def parse(self, response):
        rows = response.xpath("//div[@aria-label='data table']/table/tbody/tr")
        for r in rows:
            yield{
                'country': r.xpath(".//th/a/text()").get(),
                'year': r.xpath(".//td[1]/text()").get(),
                'debt': r.xpath(".//th[2]/text()").get(),
                'debt_percent': r.xpath(".//th[3]/text()").get(),
                'population': r.xpath(".//th[5]/text()").get()
            }
