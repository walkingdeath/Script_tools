import os,os.path,datetime
def NewFilePath():
    base_dir="F:\qgk\python\WebAutomaiton-master\WebAutomation\TestRun"
    l=os.listdir(base_dir)
    # print(l)
    l.sort(key=lambda fn: os.path.getmtime(base_dir+'\\'+fn) if not os.path.isdir(base_dir+'\\'+fn) else 0)
    return l[-2]


