# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
from tutorial.items import YouyuanItem



class YouyuanSpiderSpider(CrawlSpider):
    name = 'youyuan'
    allowed_domains = ['youyuan.com']
    start_urls = ['http://www.youyuan.com/find/guangdong/mm18-0/advance-0-0-0-0-0-0-0/p1/']
    page_lx = LinkExtractor(allow='find/guangdong/mm18-0/advance-0-0-0-0-0-0-0/p\d+/$')
    profile_lx = LinkExtractor(allow='\d*-profile/$')

    rules = [ Rule(page_lx, callback='parseList', follow=True), Rule(profile_lx, callback='parseProfile', follow=False) ]

    def parseList(self, response):
        print(response.url)

    def parseProfile(self, response):
        item = YouyuanItem()
        item['username'] = response.xpath("//div[@class='main']/strong/text()").extract()[0]
        item['header_url'] = response.xpath("//dt/img/@src").extract()[0]
        item['monologue'] = response.xpath("//ul/li/p/text()").extract()[0]
        item['summary'] = response.xpath("//p[@class='local']/text()").extract()[0]
        item['source'] = "有缘网（youyuan.om）"
        item['source'] = response.url
        yield item
