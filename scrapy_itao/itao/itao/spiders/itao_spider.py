# -*- coding: utf-8 -*-
import scrapy,json,re
from itao.js import get_collback
from itao.items import ItaoItem
callback = get_collback

class ItaoSpiderSpider(scrapy.Spider):
    name = 'itao_spider'
    allowed_domains = ['itao.com']
    #start_urls = ['https://ru.itao.com/home/ajaxHomePageScreen.htm']

    def start_requests(self):
        leimu = ['42009','42003','42002','42011','42004','42006','42006','42005','42010','42012','42013','42014','42007','42008','42001','42017']
        for i in range(len(leimu)):
            page = 0
            while page<=600:
                page +=1
                url = "https://ru.itao.com/home/ajaxHomePageScreen.htm?cateId={}&view=latest&callback={}&page={}".format(leimu[i],callback(),str(page))
                headers = {
                    'method': 'GET',
                    'authority': 'ru.itao.com',
                    'scheme': 'https',
                    'path': '/home/ajaxHomePageScreen.htm?cateId={}&view=latest&callback={}&page={}'.format(leimu[i],callback(),str(page)),
                    'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
                    'x-requested-with': 'XMLHttpRequest',
                    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
                    'referer': 'https://ru.itao.com/category/42009',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'zh-CN,zh;q=0.9'
                }
                yield scrapy.FormRequest(url,headers = headers,callback=self.parse)

    def parse(self, response):
        html = response.body
        p = re.compile(r'jQuery\d+\_\d+')
        callback_text = p.findall(html.decode('utf-8'))
        json_str = html.decode('utf-8').replace(callback_text[0],"").replace("(","").replace(")","")
        for num in range(len(json.loads(json_str)['postList'])):
            personUrl = json.loads(json_str)['postList'][num]['profileUrl']
            yield scrapy.Request(url = personUrl,callback=self.parse1)

    def parse1(self, response):
        html = response.body
        p = re.compile(r'[a-zA-Z0-9]{1,25}@[a-zA-Z0-9]{1,25}\.[a-zA-Z0-9]{1,25}')#匹配邮箱
        itaoItem = ItaoItem()

        try:
            itaoItem['url'] = str(response).replace("<", "").replace(">", "").replace("200 ", "")
            itaoItem['name'] = response.css('[id="profile-main-info-name"]::text').extract_first()
            itaoItem['email']=p.findall(html.decode('utf-8'))[0]
            if itaoItem['email'] == []:
                pass
            else:
                yield itaoItem
        except:
            pass

