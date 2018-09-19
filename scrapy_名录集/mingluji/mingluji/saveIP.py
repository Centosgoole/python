#添加代理IP,存入数据库
from redis import StrictRedis
import requests,time,random,json,re
host = "192.168.3.224"
port = "6379"
conn = StrictRedis(host = host,port = port)
timesleep = 3
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
    global timesleep
    while True:
        try:
                    #账号一免费IP
            url="http://webapi.http.zhimacangku.com/getip?num=1&type=2&pro=&city=0&yys=100017&port=1&pack=24734&ts=1&ys=0&cs=0&lb=1&sb=0&pb=45&mr=1&regions="
            #账号二免费IP
            #url="http://webapi.http.zhimacangku.com/getip?num=1&type=2&pro=&city=0&yys=100017&port=1&pack=29678&ts=1&ys=0&cs=0&lb=1&sb=0&pb=45&mr=1&regions="
            #账号一付费IP
            #url= "http://webapi.http.zhimacangku.com/getip?num=1&type=2&pro=&city=0&yys=100017&port=1&time=1&ts=1&ys=0&cs=0&lb=1&sb=0&pb=45&mr=1&regions="
            res=requests.get(url).text
            print(res)
            #判断是否出现白名单限制
            if json.loads(res)['msg'][-4:-1] == "白名单":
                q = re.compile(r'\d+\.\d+.\d+.\d+')
                write_ip = q.findall(json.loads(res)['msg'])[0]
                ipurl = "http://web.http.cnapi.cc/index/index/save_white?neek=47730&appkey=282ac6148b094806506ce5d08f171bb3&white={}".format(write_ip)
                res = requests.post(ipurl)
                if res.status_code == int("200"):
                    print("添加成功")
                else:
                    print(res.text,"\n","添加不成功")
            else:
                pass
            ipinfo =json.loads(res)['data'][0]
            ip = "{}:{}".format(ipinfo['ip'],ipinfo['port'])#获取IP
            iptime = ipinfo['expire_time']#获取IP时间
            end_time = time.mktime(time.strptime(iptime,"%Y-%m-%d %H:%M:%S"))#获取代理IP结束时间
            Now_time = time.time()#获取现在时间戳
            time_Num = end_time-Now_time#获取时间差
            timesleep=int(time_Num/60)*60#获取休息的时间
            conn.set('ip',ip)
            print("{} 存入IP：{},距离下一个IP切换还有{}分".format(time.strftime("%H:%M:%S",time.localtime()),ip,int(timesleep/60)))
            time.sleep(timesleep)
        except:
            print("啊哦....出错了...马上重新提取")
            continue

if __name__ =="__main__":
    zhimaIP()