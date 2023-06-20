import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMoviesSpider(CrawlSpider):
    name = "best_movies"
    allowed_domains = ["www.imdb.com"]
    start_urls = ['https://www.imdb.com/search/title/?genres=drama&groups=top_250&sort=user_rating,desc']

    rules = (Rule(LinkExtractor(restrict_xpaths="//h3[@class='lister-item-header']/a"), callback="parse_item", follow=True),
             Rule(LinkExtractor(restrict_xpaths='(//a[@class="lister-page-next next-page"])[1]'))
             )

    def parse_item(self, response):
        # print(response.url)
        yield{
            'title':response.xpath("//h1/span/text()").get(),
            'year':response.xpath("(//ul/li[@class='ipc-inline-list__item'][1])[2]/a/text()").get(),
            'duration':response.xpath("(//ul/li[@class='ipc-inline-list__item'][3])[2]/text()").get(),
            'genre':response.xpath("(//ul/li[@class='ipc-inline-list__item'][2])[2]/a/text()").get(),
            'rating':response.xpath("//div[@data-testid='hero-rating-bar__aggregate-rating__score']/span[1]/text()").get(),
            'movie_url':response.url
        }