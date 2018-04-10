import os,os.path,datetime
base_dir="F:\qgk\python\WebAutomaiton-master\WebAutomation\TestRun"
l=os.listdir(base_dir)
# print(l)
l.sort(key=lambda fn: os.path.getmtime(base_dir+'\\'+fn) if not os.path.isdir(base_dir+'\\'+fn) else 0)
print(l)
d=datetime.datetime.fromtimestamp(os.path.getmtime(base_dir+'\\'+l[-2]))
print('最后改动的文件是'+l[-2]+"，时间："+d.strftime("%Y%m%d %H%M%S"))
