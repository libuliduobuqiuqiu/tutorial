from scrapy.spiders import Spider
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess


class ExampleSpider(Spider):
    name = "example"
    allowed_domains = ['example.com']
    start_urls = ['http://example.com']

    def __init__(self, flag=None, *args, **kwargs):
        super(Spider, self).__init__(*args, **kwargs)
        print("Flag %s" % flag)
        print(args)
        print(kwargs)

    def parse(self, response):
        print('Existing Settings: %s' % self.settings.attributes.keys())
        print("Existing Log_File Path: %s" % self.settings.get('LOG_FILE'))

def run_example_spider():
    # 用脚本启动spider
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    process.crawl('example')
    process.start()

if __name__ == "__main__":
    run_example_spider()
