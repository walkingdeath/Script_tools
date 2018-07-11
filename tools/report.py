#!/usr/bin/python
# -*- coding: UTF-8 -*-
import itchat
import requests
import json
import time
# from openpyxl import Workbook
from openpyxl import load_workbook


# def bustil_login():



def search_bustil_interface(statusList):
    headers = {'token': '1107c74adada4a84a9f7a2f9bef36b64',
               'connection': 'keep-alive'
               }
    url = 'http://47.100.97.254/api/chargerorder/queryList'
    data = '2018-07-09'
    payload = {'current': 1,'beginTime':'%s'%data,'endTime':'%s'%data,'statusList':'%s'%statusList,'menuValue': 'orderId'}
    r = requests.get(url, headers=headers, params=payload)
    # print(r.text)
    r_dict = json.loads(r.text)
    records_list = r_dict['data']['records']
    return records_list


def search_pingxx_interface(channel):
    headers = {'Authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjUzNTIsInJhbmRvbSI6IjFtdlBlMTE4In0.LCSHTrY74uEp3nUGCreU_5Z9BztnXdyQkSsEp4QM-Kc',
               'connection':'keep-alive'
               }
    url = 'https://dashboard2.pingxx.com/api/charge/list'
    data = '2018-07-09'
    payload = {
               'app_id':'app_54CW1Cv1qvjDffzn',
               'from_time':'1531065600',
               'to_time':'1531151999',
               'channel':'%s'%channel,
               'live_mode':1,
               'paid':1,
               'currency':'cny'
               }
    r = requests.get(url, headers=headers, params=payload)
    # print(r.text)
    r_dict = json.loads(r.text)
    return r_dict



def sum_orderElectricity():
    statusList = '2000,800'
    records_list = search_bustil_interface(statusList)
    if len(records_list) != 0:
        sum = [0,]
        for list in records_list:
            # print(list["orderElectricity"])
            # print(sum[0])
            sum[0] = sum[0] + list["orderElectricity"]
        print(sum[0]/100)
        return sum[0]/100


def sum_order_payment():
    pass


def sum_order_accout():
    pass


def sum_wechat_amount_count():
    channel = 'wx*wx_pub*wx_pub_scan*wx_pub_qr'
    r_dict = search_pingxx_interface(channel)
    sum = [0,0]
    charge_paid_count = r_dict['data']['message']['summary']['charge_paid_count']
    charge_paid_amount = r_dict['data']['message']['summary']['charge_paid_amount']
    return charge_paid_amount/100, charge_paid_count


def sum_alipay_amount_count():
    channel = 'alipay'
    r_dict = search_pingxx_interface(channel)
    charge_paid_count = r_dict['data']['message']['summary']['charge_paid_count']
    charge_paid_amount = r_dict['data']['message']['summary']['charge_paid_amount']
    return charge_paid_amount/100, charge_paid_count


def sum_order_not_pay():
    statusList = '800'
    records_list = search_bustil_interface(statusList)
    if len(records_list) != 0:
        sum = [0,0]
        for list in records_list:
            print(list['orderPrice'])
            sum[0] = sum[0] + 1
            sum[1] = sum[1] + list['orderPrice']
        print(sum[1]/100)
        return sum[0], sum[1]/100


def input_xlxs():
    sh = ['7月9日', sum_orderElectricity(), sum_wechat_amount_count()[0], sum_wechat_amount_count()[1], sum_alipay_amount_count()[0], sum_alipay_amount_count()[1],
          sum_order_not_pay()[0], sum_order_not_pay()[1]]
    print(sh)
    wb = load_workbook('Summary_of_platform.xlsx')
    sheet = wb.active
    sheet['A11'] = sh[0]
    # print(sh[0])
    sheet['B11'] = sh[1]
    # sheet['C11'] = sh[0]
    # sheet['D11'] = sh[0]
    sheet['E11'] = sh[2]
    sheet['F11'] = sh[3]
    sheet['G11'] = sh[4]
    sheet['H11'] = sh[5]
    # sheet['I11'] = sh[0]
    # sheet['J11'] = sh[0]
    # sheet['K11'] = sh[0]
    # sheet['L11'] = sh[0]
    sheet['M11'] = sh[6]
    sheet['N11'] = sh[7]
    wb.save('Summary_of_platform.xlsx')


if __name__ == "__main__":
    # search_interface()
    # sum_orderElectricity()
    # input_xlxs()
    # search_pingxx_interface()
    # sum_wechat_payment()
    input_xlxs()
