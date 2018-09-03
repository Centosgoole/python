# -*- coding: utf-8 -*-
import scrapy
from mingluji.items import MinglujiItem

class DenmarkSpiderSpider(scrapy.Spider):
    name = 'Denmark_spider'
    allowed_domains = ['dnk.bizdirlib.com']
    start_urls = ['http://dnk.bizdirlib.com/company']

    def parse(self, response):#获取url
        url_list = response.xpath('//*[@id="block-system-main"]/div/div/div[2]/div/ul/li')
        for i in range(len(url_list)):
            link = "https://dnk.bizdirlib.com"+str(response.xpath('//*[@id="block-system-main"]/div/div/div[2]/div/ul/li['+str(i)+']/div/span/a/@href').extract_first())
            yield scrapy.Request(link,callback=self.prase1)
        next_link = response.xpath('//*[@id="block-system-main"]/div/div/div[3]/ul/li[3]/a/@href').extract_first()#获取下一页
        if next_link:
            next_link = next_link
            yield scrapy.Request("https://dnk.bizdirlib.com"+next_link,callback=self.parse)
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
