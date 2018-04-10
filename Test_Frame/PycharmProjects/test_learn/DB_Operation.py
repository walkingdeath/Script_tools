import pymysql
class MysqldbHelper:
    def getCon(self):
        try:
            conn = pymysql.connect(host = '192.168.16.122',user = 'root',passwd = '123456',db = 'python',port = 3306,charset = 'utf8' )