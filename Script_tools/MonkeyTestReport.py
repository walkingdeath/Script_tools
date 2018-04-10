#coding=utf-8

'''
 Create on 2016-05-18
 python 3.4 for window
 @auther: qiuguangkang
'''
import os
import sys
import time

class monkeyTest():

     def __init__(self):
         """ init """

    #monkey命令，packageName包名，interval间隔时间单位ms ，frequency执行次数
     def monkeyApp(self,packageName,interval,frequency):
        try:
             #os.popen("adb shell monkey -p {0} --throttle {1} --ignore-crashes --ignore-timeouts --ignore-security-exceptions --ignore-native-crashes \
             #--monitor-native-crashes -v -v -v {2}> E:\MonkeyTest\MonkeyTestReport\monkeyScreenLog.log".format(packageName,interval,frequency) ,'r')
             print(packageName)
             print(interval)
             print(frequency)
             print('正在执行monkey程序')
        except Exception as e:

            print (e)

     #导出日志
     def copyErrorLog(self):
        try:
            anr = "E:\\MonkeyTest\\monkeylog\\anr"
            if not os.path.isdir(anr):
                os.makedirs(anr)
                dontpanic = "E:\\MonkeyTest\\monkeylog\\dontpanic"
            if not os.path.isdir(dontpanic):

                os.makedirs(dontpanic)
                tombstones = "E:\\MonkeyTest\\monkeylog\\tombstones"
            if not os.path.isdir(tombstones):

                os.makedirs(tombstones)
                bugreports = "E:\\MonkeyTest\\monkeylog\\bugreports"
            if not os.path.isdir(bugreports):
                 os.makedirs(bugreports)
            os.popen("adb pull /data/anr  E://MonkeyTest//monkeylog//anr",'r')
            os.popen("adb pull /data/dontpanic  E://MonkeyTest//monkeylog//dontpanic",'r')
            os.popen("adb pull /data/tombstones  E://MonkeyTest//monkeylog//tombstones",'r')
            os.popen("adb pull /data/data/com.android.shell/files/bugreports  E://MonkeyTest//monkeylog//bugreports",'r')
        except Exception as e:

             print (e)

def main():
     print ("""""")

if __name__=="__main__":
     AppDict = {'H300L':'com.microsenstech.H300L','HeartHealth':'com.microsens.hearthealth','uCare6min':'com.microsenstech.ucarerg'}
     AppName = ''
     packageName = ''
     try:
         AppName = input('请输入被测软件名字：')
         packageName = AppDict[AppName]
     except KeyError :
         print ('你输入的软件名'+AppName+'不存在，请核实')


     #packageName = 'com.microsens.hearthealth'
     myApp = monkeyTest()
     myApp.monkeyApp(packageName,500,10000)
     #判断是否执行完成，执行完成后导出日志
     for i in range(1, 1000000):
         monkeylog = open('E:\MonkeyTest\MonkeyTestReport\monkeyScreenLog.log')
         try:
             temp = monkeylog.read( )
         finally:
             monkeylog.close( )
         if temp.count('Monkey finished')>0:
             myApp.copyErrorLog()
             print('Monkey测试已经完成')
             break
         else:
             time.sleep(2)