from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class BitshareSpider(CrawlSpider):
    name = "bitshare"
    allowed_domains = ['bitsharestalk.org']
    start_urls = ["https://bitsharestalk.org/index.php?board=4.0"]

    nextpage_lx = LinkExtractor(allow = ('https://bitsharestalk\.org/index\.php\?board=\d+\.\d+$', "https://bitsharestalk\.org/index\.php\?PHPSESSID\S*board=\d+\.\d+$"))
    topicpage_lx = LinkExtractor(allow = ( " https://bitsharestalk\.org/index\.php\?PHPSESSID\S*topic=\d+\.\d+$" ,  "https://bitsharestalk\.org/index\.php\?topic=\d+\.\d+$", ))
    rules = [ Rule(nextpage_lx, process_links = 'linkfiltering', callback='parseContent', follow=True), Rule(topicpage_lx, process_links = 'linkfiltering', follow=True) ]

    def linkfiltering(self, links):
        ret = [] 
        
        for link in links:
            url = link.url
            print(url)
            urlfirst, urllast = url.split('?')

            if urllast:
                link.url = urlfirst +"?"+ urllast.split('&', 1)[-1]
        return links

    def parseContent(self, response):
        items = response.xpath("//tr/td/div/span/a/text()")

        for item in items:
            print(item.extract())
        

