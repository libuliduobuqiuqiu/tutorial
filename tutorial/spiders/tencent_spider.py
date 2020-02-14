from scrapy import spiders
from urllib.parse import urlencode
import time
import json

from tutorial.items import TutorialItem


class RecruitSpier(spiders.Spider):
    name = "tencent"
    timestamp = int(time.time())
    allowed_domains = ['careers.tencent.com']
    params = {'timestamp': timestamp, 'countryId': "", 'cityId':"", 'bgIds':"", 'productId':"", "categoryId":"",
            "parentCategoryId":"", "attrId":"", "keyword":"", "pageIndex": 1, "pageSize": 10, "language": "zh-cn",
            "area": "cn"}
    base_url = "https://careers.tencent.com/tencentcareer/api/post/Query?" + urlencode(params)
    start_urls = [ base_url ]


    def parse(self, response):
        jobs = json.loads(response.text)
        for job in jobs['Data']['Posts']:
            jobname = job['RecruitPostName']
            country = job['CountryName']
            city = job['LocationName']
            productname = job['ProductName']
            categoryname = job['CategoryName']
            responsibility = job['Responsibility']
            updatetime = job['LastUpdateTime']

            result = {}
            result = {'jobname': jobname, 'country': country, 'city': city,
                    'productname': productname, 'categoryname': categoryname,
                    'responsibility': responsibility, 'updatetime': updatetime}
            print(result)            

            item = TutorialItem()
            item['jobname'] = jobname
            item['country'] = country
            item['city'] = city
            item['productname'] = productname
            item['categoryname'] = categoryname
            item['responsibility'] = responsibility
            item['updatetime'] = updatetime
            yield item        

