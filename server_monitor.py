#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#author  libertyspy
import socket
#import smtplib
import urllib.request
import smtplib
import email.mime.multipart
import email.mime.text
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time




'''
mail_options = {
    'server':'smtp.qq.com',#使用了QQ的SMTP服务，需要在邮箱中设置开启SMTP服务
    'port':25,             #端口
    'user':'hacker@qq.com',#发送人
    'pwd':'hacker',        #发送人的密码
    'send_to':'sniper@qq.com',  #收件者
}
'''
'''
msg_options={
    'user':'hacker',    #短信平台的用户名
    'pwd':'74110',      #短信平台的密码
    'phone':'12345678910',   #需要发短信的电话号码
}
'''




test_host = 'http://122.0.75.174/zentao/my/'
#test_host = "https://www.baidu.com/"
def url_request(host,port=80):
    try:
        response = urllib.request.urlopen(host)
        response_code = response.getcode()
        if 200 != response_code:
            return response_code
        else:
            return True
    except IOError as e:
        return False




'''
def send_message(msg,host,status):
    send_msg='服务器:%s挂了！状态码：%s' % (host,status)
    request_api="http://www.uoleem.com.cn/api/uoleemApi?username=%s&pwd=%s&mobile=%s&content=%s"  \
            % (msg['user'],msg['pwd'],msg['phone'],send_msg)
    return url_request(request_api)
'''
'''
def send_email(mail,host,status):
    smtp = smtplib.SMTP()
    smtp.connect(mail['server'], mail['port'])
    smtp.login(mail['user'],mail['pwd'])
    msg="From:%s\rTo:%s\rSubject:服务器: %s 挂了 !状态码:%s\r\n" \
         % (mail['user'],mail['send_to'],host,status)
    smtp.sendmail(mail['user'],mail['send_to'], msg)
    smtp.quit()
'''





def send_email():
    # 第三方 SMTP 服务
    mail_host="smtp.qq.com"  #设置服务器
    mail_user="@qq.com"    #用户名
    mail_pass='******'   #口令

    sender = '812110590@qq.com'
    #receivers = ['@qq.com','@qq.com','@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    receivers = ['812110590@qq.com']
    message = MIMEText('禅道网站当机了', 'plain', 'utf-8')
    message['From'] = Header("系统", 'utf-8')
    message['To'] =  Header("测试", 'utf-8')

    subject = '禅道网络运行状况'
    message['Subject'] = Header(subject, 'utf-8')


    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
        smtpObj.login(mail_user,mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print ("邮件发送成功")
    except smtplib.SMTPException:
        print ("Error: 无法发送邮件")

def check_status(host,port=80):
    s = socket.socket()
    ret_msg = []
    try:
        s.connect((host,port))
        return True
    except socket.error as e:
        return False

if __name__=='__main__':
    print('正在监控禅道网站......')
    print('每半小时会邮件通知网站情况')
    while True :
        status = url_request(test_host)
        if status is not True and status is not None:
            send_email()
            print("Server is down")
            time.sleep(1800)
            #send_email(mail_options,test_host,status)
           # send_message(msg_options,test_host,status)
        else:
            print("网站正常运行")
            time.sleep(1800)