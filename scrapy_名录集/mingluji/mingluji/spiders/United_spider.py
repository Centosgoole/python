# -*- coding: utf-8 -*-
import scrapy
from mingluji.items import MinglujiItem
from scrapy_redis.spiders import RedisSpider

#class UnitedSpiderSpider(scrapy.Spider):
class UnitedSpiderSpider(RedisSpider):
    name = 'United_spider'
    allowed_domains = ['unitedkingdom.bizdirlib.com']
    #start_urls = ['http://unitedkingdom.bizdirlib.com/company']
    redis_key = 'United_spider:start_urls'
    def parse(self, response):#获取url
        # cookies = {
        #     '__utmz': '21043177.1534837336.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
        #     'OUTFOX_SEARCH_USER_ID_NCOO': '2078409329.1983817',
        #     '__utma': '21043177.658691249.1534837336.1534979391.1534991379.4',
        #     'has_js': '1',
        #     '__utmc': '21043177',
        #     '__utmt': '1',
        #     '__utmb': '21043177.11.10.1534991379',
        #     '__atuvc': '45%7C34',
        #     '__atuvs': '5b7e1c12c9f97d7400a'
        # }
        url_list = response.xpath('//*[@id="block-system-main"]/div/div/div[2]/div/ul/li')
        for i in range(len(url_list)):
            link = "https://unitedkingdom.bizdirlib.com"+str(response.xpath('//*[@id="block-system-main"]/div/div/div[2]/div/ul/li['+str(i)+']/div/span/a/@href').extract_first())
            yield scrapy.Request(link,callback=self.prase1)
        next_link = response.xpath('//*[@id="block-system-main"]/div/div/div[3]/ul/li[3]/a/@href').extract_first()#获取下一页
        if next_link:
            next_link = next_link
            yield scrapy.Request("https://unitedkingdom.bizdirlib.com"+next_link,callback=self.parse)

    def prase1(self,response):#解析内容
        if response.css('[itemprop="email"]::text').extract_first() !=None:
            Category_html = response.css("fieldset ul li").extract()
            try:
                Category_text = re.findall(r"<strong>Category Activities</strong>(.*?)</li>", str(Category_html))[0].split(":")[1].replace(" ","")
            except:
                Category_text = None
            minglujiurl = MinglujiItem()
            minglujiurl['Company_Name'] = response.css('[itemprop="name"]::text').extract_first()
            minglujiurl['Country'] = response.css('[itemprop="location"]::text').extract_first()
            minglujiurl['Address'] = response.css('[itemprop="address"]::text').extract_first()
            minglujiurl['Phone'] = response.css('[itemprop="telephone"]::text').extract_first()
            minglujiurl['Email'] = response.css('[itemprop="email"]::text').extract_first()
            minglujiurl['web_url'] = response.css('[itemprop="url"]::text').extract_first()
            minglujiurl['Category'] = Category_text
            yield minglujiurl
        else:
            pass
