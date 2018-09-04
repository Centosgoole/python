#添加代理IP,存入数据库
from redis import StrictRedis
import requests,time
host = "192.168.3.224"
port = "6379"
conn = StrictRedis(host = host,port = port)
#请求代理IP
def data5ip():#代理无忧
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
def zhimaIP():#芝麻代理IP
    url= "http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=&city=0&yys=0&port=1&pack=24734&ts=0&ys=0&cs=0&lb=4&sb=0&pb=4&mr=1&regions="
    ip=requests.get(url).text.split("\n")[0]
    conn.set('ip',ip)
    print("存入IP：{}".format(ip))

if __name__ =="__main__":
    zhimaIP()