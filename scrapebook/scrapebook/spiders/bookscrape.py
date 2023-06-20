import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BookscrapeSpider(CrawlSpider):
    name = "bookscrape"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    rules = (Rule(LinkExtractor(restrict_xpaths='//h3/a'), callback="parse_item", follow=True),
             Rule(LinkExtractor(restrict_xpaths="//a[normalize-space()='next']"))
             )

    def parse_item(self, response):
        yield{
            "Book_name":response.xpath("//h1/text()").get(),
            "Price":response.xpath("//p[normalize-space()='£37.59']/text()").get(),
            "Availability":response.xpath("//th[normalize-space()='Availability']/following-sibling::td[1]/text()").get(),
            "UPC":response.xpath("//th[normalize-space()='UPC']/following-sibling::td[1]/text()").get(),
            "Genre":response.xpath("(//ul[@class='breadcrumb']/li/a)[last()]/text()").get(),
            "Image_URL":response.urljoin(response.xpath("//div[@class='item active']/img/@src").get()),
            'Book_URL':response.url
        }
        