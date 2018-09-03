#添加代理IP,存入数据库
from redis import StrictRedis
import requests,time
host = "192.168.3.224"
port = "6379"
conn = StrictRedis(host = host,port = port)
#请求代理IP
while True:
    try:
        url = "http://api.ip.data5u.com/dynamic/get.html?order=8233980a3ef013f471ec8331602dc174&sep=3"
        res = requests.get(url).text
        ip = res.split('\n')[0]
        conn.set('ip',ip)
        print("存入IP：{}".format(ip))
        time.sleep(15)
    except:
        pass
        continue
