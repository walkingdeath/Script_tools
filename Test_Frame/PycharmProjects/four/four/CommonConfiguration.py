from _datetime import datetime
class CommonConfiguration(object):

    #设置driverPath路径
    # def driverPath(self):
    #     return r'C:\Users\xua\Downloads\chromedriver_win32\chromedriver.exe'

    def baseUrl(self):
        return "http://172.16.34.150:81/#/login"

    #change time to str

    def getCurrentTime(self):
        format = "%a %b %d %H:%M:%S %Y"
        return datetime.now().strftime(format)

    # Get time diff
    def timeDiff(self,starttime,endtime):
        format = "%a %b %d %H:%M:%S %Y"
        return datetime.strptime(endtime,format) - datetime.strptime(starttime,format)