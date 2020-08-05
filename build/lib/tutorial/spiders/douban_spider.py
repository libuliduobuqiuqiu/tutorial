from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import scrapy
import logging

from tutorial.items import DoubanItem

logger = logging.getLogger("Administrator")
class DoubanSpider(CrawlSpider):
    name = "douban"
    allowed_domains = ["movie.douban.com"]
    start_urls = ["https://movie.douban.com/subject/25931446/comments?status=P"]
    page_lx = LinkExtractor(allow=('\?start'))
    rules = [ Rule(page_lx, callback='parsecontent', follow=True) ]

    def parsecontent(self, response):
        comments = response.xpath("//div[@class='comment']")
        for comment in comments:
            item = DoubanItem()
            item['username'] = comment.xpath("./h3/span[@class='comment-info']/a/text()").extract()[0]
            item['comment'] = comment.xpath("./p/span/text()").extract()[0]
            item['updatetime'] = comment.xpath("./h3/span[@class='comment-info']/span[contains(@class, 'comment-time')]/text()").extract()[0].strip('\n| ')
            logger.info("Comment Username: %s" % item['username'])
            # print(item['username'], item['comment'], item['updatetime'])
            yield item

