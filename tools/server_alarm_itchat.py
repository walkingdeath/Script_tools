#!/usr/bin/python
# -*- coding: UTF-8 -*-
import itchat
import requests
import json
import time


def login_WeChat():
    itchat.auto_login(hotReload=True)
	itchat.auto_login(enableCmdQR=True)
	#itchat.auto_login()


def sendalarm_to_friend():
    name = itchat.search_friends(name=u'宣蓉')
    print(name)
    print(len(name))
    xuanrong = name[0]["UserName"]
    print(xuanrong)
    itchat.send(u'快睡觉啦', xuanrong)
    print(u'发送成功')


def sendalarm_to_group():
    chatrooms = itchat.search_chatrooms(name=u'普斯迪尔研发中心')
    print(chatrooms)
    yanfazhongxin = chatrooms[0]["UserName"]
    print(yanfazhongxin)
    itchat.send(u'线上---系统出现超过10以上异常订单，请关注---%s' % {time.strftime("%H:%M:%S")}, yanfazhongxin)
    print(u'信息已经发送到研发中心微信群')


def sendalarm_by_email():
    pass


def sum_exception_order():
    alarm_num = [0, ]
    exce_order_list = []
    headers = {'token': 'b091d4f096b5460a9da7b32b53505379'}
    url = 'http://47.100.97.254/api/chargerorder/queryList'
    payload = {'size': 20, 'current': 1, 'menuValue': 'orderId'}
    r = requests.get(url, headers=headers, params=payload)
    r_dict = json.loads(r.text)
    print(r_dict)
    print(type(r_dict))
    print(r_dict['message'])
    print(r_dict['data']['records'])
    records_list = r_dict['data']['records']
    # print(len(records_list))
    if len(records_list) != 0:
        for record in records_list:
            if record['status'] < 0:
                alarm_num[0] = alarm_num[0] + 1
                exce_order_list.append(record['orderId'])
    return alarm_num[0], exce_order_list


def sendalarm_or_not():
    alarm_order_list = sum_exception_order()
    print(u'异常订单数量%s，异常订单号%s' % (alarm_order_list[0], alarm_order_list[1]))
    if alarm_order_list[0] >= 10:
        sendalarm_to_group()
    else:
        print(u'异常订单不超过10个，系统正常')



if __name__ == "__main__":
    print(u'****开始监控异常订单****')
    login_WeChat()
    # sendalarm_to_friend()
    # sendalarm_to_group()
    # sum_exception_order()
    while True:

        sendalarm_or_not()
        print(u'每隔20分钟检测异常订单，当前时间---%s' % (time.strftime("%H:%M:%S")))
        time.sleep(1200)
