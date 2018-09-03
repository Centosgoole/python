# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from mingluji.settings import mongo_host,mongo_port,mongo_db_name
class MinglujiPipeline(object):
    #初始化mongodb的变量
    def __init__(self):
        host = mongo_host
        port = mongo_port
        db_name = mongo_db_name
        conn = pymongo.MongoClient(host = host,port = port)
        mydb = conn[db_name]
        self.post = mydb["Europe_data"]
    '''
    创建保存的方法，必须传入两个参数，item和spider两个参数
    item:spider生成的item
    spider:spider的实例
    '''
    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item
