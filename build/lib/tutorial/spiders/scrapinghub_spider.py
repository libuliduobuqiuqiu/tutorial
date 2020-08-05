from scrapy.spiders import Spider
import scrapy


class ScrapinghubSpider(Spider):
    name = "scrapinghub"
    allowed_domains = ['scrapinghub.com']
    start_urls = ['https://scrapinghub.com/']

    def parse(self, response):
        url = response.url
        self.logger.info("Parse function called on: %s" % url)

    
