import scrapy


class GdpDebtSpider(scrapy.Spider):
    name = "gdp_debt"
    allowed_domains = ["worldpopulationreview.com"]
    start_urls = ["https://worldpopulationreview.com/country-rankings/countries-by-national-debt/"]

    def parse(self, response):
        rows = response.xpath("//table/tbody/tr[position()>1]")
        for r in rows:
            yield{
                'rank': r.xpath(".//td[1]/text()").get(),
                'country': r.xpath(".//td[2]/a/text()|.//td[2]/text()").get(),
                'debt': r.xpath(".//td[3]/text()").get()
                #'debt_percent': r.xpath(".//td[3]/text()").get(),
                #'population': r.xpath(".//td[5]/text()").get()
            }
