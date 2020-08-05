from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from tutorial.items import SunItem

class SunSpider(CrawlSpider):
    name = "sun"
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=']

    next_page =  LinkExtractor(allow=('http://wz\.sun0769\.com/index\.php/question/questionType\?type=\d+&page=\d*'))
    content_page =  LinkExtractor(allow=("http://wz\.sun0769\.com/html/question/\d+/\d+.shtml"))
    rules = [ Rule(next_page, follow=True), Rule(content_page, callback='parseContent', follow=True) ]

    def parseContent(self, response):
        print(response.url)
        item = SunItem()

        item['title'] = response.xpath("//span[@class='niae2_top']/text()")[0].extract()
        item['status'] = response.xpath("//div[@class='wzy3_1']/span/text()").extract()[0]
        item['content'] = response.xpath("//td[@class='txt16_3']/text()").extract()[0]
        item['detail'] = response.xpath("//div[@class='wzy3_2']/span/text()")[0].extract()

        yield item



