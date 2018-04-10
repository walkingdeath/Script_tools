#!/user/bin/env python
#coding=utf-8
import requests
import datetime
import time
import threading
import json
class url_request():
    times = []
    error = []
    def req(self,Password,Rm,username):
        myreq=url_request()
        headers = {'content-type': 'application/json','User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
        payload = {"password":Password,"rememberMe":Rm,"username":username}
        r = requests.post("http://10.165.33.20:8090/api/authenticate",headers=headers,data = json.dumps(payload))
        ResponseTime=float(r.elapsed.microseconds)/1000 #获取响应时间，单位ms
        print(ResponseTime)
        myreq.times.append(ResponseTime) #将响应时间写入数组
        if r.status_code !=200 :
            myreq.error.append("0")
            #print(myreq.error)  #打印错误数组

if __name__=='__main__':
    myreq=url_request()
    threads = []
    starttime = datetime.datetime.now()
    print "request start time %s" %starttime
    nub = 50#设置并发线程数
    ThinkTime = 0.05#设置思考时间
    for i in range(1, nub+1):
        t = threading.Thread(target=myreq.req, args=('admin',True,'admin'))
        threads.append(t)
    for t in threads:
        time.sleep(ThinkTime)
        #print "thread %s" %t #打印线程
        t.setDaemon(True)
        t.start()
    t.join()
    endtime = datetime.datetime.now()
    print "request end time %s" %endtime
    #time.sleep(3)
    AverageTime = "{:.3f}".format(float(sum(myreq.times))/float(len(myreq.times))) #计算数组的平均值，保留3位小数
    print "Average Response Time %s ms" %AverageTime #打印平均响应时间
    usetime = str(endtime - starttime)
    hour = usetime.split(':').pop(0)
    minute = usetime.split(':').pop(1)
    second = usetime.split(':').pop(2)
    totaltime = float(hour)*60*60 + float(minute)*60 + float(second) #计算总的思考时间+请求时间
    print "Concurrent processing %s" %nub #打印并发数
    print "use total time %s s" %(totaltime-float(nub*ThinkTime)) #打印总共消耗的时间
    print "fail request %s" %myreq.error.count("0") #打印错误请求数