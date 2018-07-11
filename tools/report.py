#!/usr/bin/python
# -*- coding: UTF-8 -*-
import itchat
import requests
import json
import time
# from openpyxl import Workbook
from openpyxl import load_workbook


def search_bustil_interface(statuslist):
    headers = {'token': '1107c74adada4a84a9f7a2f9bef36b64',
               'connection': 'keep-alive'
               }
    url = 'http://47.100.97.254/api/chargerorder/queryList'
    data = '2018-07-09'
    payload = {'current': 1, 'beginTime': '%s' % data, 'endTime': '%s' % data,
               'statusList': '%s' % statuslist, 'menuValue': 'orderId'}
    r = requests.get(url, headers=headers, params=payload)
    # print(r.text)
    r_dict = json.loads(r.text)
    records_list = r_dict['data']['records']
    return records_list


def search_pingxx_interface(channel):
    headers = {'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjUzNTIsInJhbmRvbSI6InY1MDhLU2FmIn0.qZubfF-idk5D1wCQXDzopIA7dFTnbNF9R1NtCnVoRqk',
               'connection': 'keep-alive'
               }
    url = 'https://dashboard2.pingxx.com/api/charge/list'
    data = '2018-07-09'
    payload = {
               'app_id': 'app_54CW1Cv1qvjDffzn',
               'from_time': '1531065600',
               'to_time': '1531151999',
               'channel': '%s' % channel,
               'live_mode': 1,
               'paid': 1,
               'currency': 'cny'
               }
    r = requests.get(url, headers=headers, params=payload)
    # print(r.text)
    r_dict = json.loads(r.text)
    return r_dict


def sum_orderElectricity():
    statuslist = '2000,800'
    records_list = search_bustil_interface(statuslist)
    if len(records_list) != 0:
        sum = [0, ]
        for list in records_list:
            # print(list["orderElectricity"])
            # print(sum[0])
            sum[0] = sum[0] + list["orderElectricity"]
        # print(sum[0]/100)
        return sum[0]/100


def sum_order_amount_count():
    statuslist = '2000'
    records_list = search_bustil_interface(statuslist)
    if len(records_list) != 0:
        sum = [0, 0]
        for list in records_list:
            sum[0] = sum[0] + list["orderPrice"]
            sum[1] = sum[1] + 1
        return sum[0]/100, sum[1]


def sum_wechat_amount_count():
    channel = 'wx*wx_pub*wx_pub_scan*wx_pub_qr'
    r_dict = search_pingxx_interface(channel)
    sum_recharge_list = [0, 0]
    for i in r_dict['data']['message']['list']:
        if i['amount'] % 10000 == 0:
            sum_recharge_list[0] = sum_recharge_list[0] + i['amount']
            sum_recharge_list[1] = sum_recharge_list[1] + 1
        else:
            pass
    charge_paid_amount = r_dict['data']['message']['summary']['charge_paid_amount'] - sum_recharge_list[0]
    charge_paid_count = r_dict['data']['message']['summary']['charge_paid_count'] - sum_recharge_list[1]
    return charge_paid_amount/100, charge_paid_count, sum_recharge_list[0], sum_recharge_list[1]


def sum_alipay_amount_count():
    channel = 'alipay'
    r_dict = search_pingxx_interface(channel)
    sum_recharge_list = [0, 0]
    for i in r_dict['data']['message']['list']:
        if i['amount'] % 10000 == 0:
            sum_recharge_list[0] = sum_recharge_list[0] + i['amount']
            sum_recharge_list[1] = sum_recharge_list[1] + 1
        else:
            pass
    charge_paid_amount = r_dict['data']['message']['summary']['charge_paid_amount'] - sum_recharge_list[0]
    charge_paid_count = r_dict['data']['message']['summary']['charge_paid_count'] - sum_recharge_list[1]
    return charge_paid_amount/100, charge_paid_count, sum_recharge_list[0], sum_recharge_list[1]


def sum_order_not_pay():
    statuslist = '800'
    records_list = search_bustil_interface(statuslist)
    if len(records_list) != 0:
        sum = [0, 0]
        for list in records_list:
            # print(list['orderPrice'])
            sum[0] = sum[0] + 1
            sum[1] = sum[1] + list['orderPrice']
        # print(sum[1]/100)
        return sum[0], sum[1]/100


def input_xlxs():
    print(u'正在收集数据。。。')
    sum_recharge_list = [sum_wechat_amount_count()[2] + sum_alipay_amount_count()[2],
                         sum_wechat_amount_count()[3] + sum_alipay_amount_count()[3]]
    excel = ['7月9日', sum_orderElectricity(), sum_wechat_amount_count()[0], sum_wechat_amount_count()[1], sum_alipay_amount_count()[0],
             sum_alipay_amount_count()[1], sum_recharge_list[0], sum_recharge_list[1], sum_order_not_pay()[0], sum_order_not_pay()[1]]
    print(excel)
    print(u'完成数据查询，开始数据录入excel')
    wb = load_workbook('Summary_of_platform.xlsx')
    sheet = wb.active
    sheet['A11'] = '7月9日'
    sheet['B11'] = sum_orderElectricity()
    sheet['C11'] = sum_order_amount_count()[0]
    sheet['D11'] = sum_order_amount_count()[1]
    sheet['E11'] = sum_wechat_amount_count()[0]
    sheet['F11'] = sum_wechat_amount_count()[1]
    sheet['G11'] = sum_alipay_amount_count()[0]
    sheet['H11'] = sum_alipay_amount_count()[1]
    # sheet['I11'] = sh[0]
    # sheet['J11'] = sh[0]
    sheet['K11'] = (sum_wechat_amount_count()[2] + sum_alipay_amount_count()[2])/100
    sheet['L11'] = sum_wechat_amount_count()[3] + sum_alipay_amount_count()[3]
    sheet['M11'] = sum_order_not_pay()[0]
    sheet['N11'] = sum_order_not_pay()[1]
    wb.save('Summary_of_platform.xlsx')
    print(u'完成excel数据录入')


def send_mail():
    pass


if __name__ == "__main__":
    # search_interface()
    # sum_orderElectricity()
    # input_xlxs()
    # search_pingxx_interface()
    # sum_wechat_payment()
    input_xlxs()
