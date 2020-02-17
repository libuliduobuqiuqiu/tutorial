from scrapy import cmdline


cmdline.execute("scrapy crawl example -a flag=sb -o example.json -t json".split())
# 直接命令调试
