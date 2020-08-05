from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from tutorial.items import SunItem

class SunSpider(CrawlSpider):
    name = "sun"
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/political/index/politicsNewest?id=1&page=1']

    next_page = LinkExtractor(allow=('http://wz\.sun0769\.com/political/index/politicsNewest\?id=1&page=\d*'))
    content_page = LinkExtractor(allow=("http://wz\.sun0769\.com/political/politics/index\?id=\d*"))
    rules = [ Rule(next_page, follow=True), Rule(content_page, callback='parseContent', follow=True) ]

    def parseContent(self, response):
        print(response.url)
        item = SunItem()

        item['title'] = response.xpath("//p[@class='focus-details']/text()")[0].extract()
        status = response.xpath("//span[@class='fl'][2]/text()").extract()[0]
        item['status'] = "".join(status.split())
        item['content'] = response.xpath("//div[@class='mr-three']/div[@class='details-box']/pre/text()").extract()[0]
        pubdate = response.xpath("//span[@class='fl'][1]/text()")[0].extract()
        item['pubdate'] = "".join(pubdate.split("发布日期"))

        yield item



