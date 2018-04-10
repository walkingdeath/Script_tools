import smtplib
import string
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE,formatdate
from _datetime import datetime
# from WebAutomation.CommonLibrary import ResultFolder
from WebAutomation.CommonLibrary import NewModifyTime


def send_email(send_from,send_to,password,subject,text,files=None,server="smtp.qq.com"):

    #assert(isinstance(send_to,list),"Send To email should be a list")
    # print(send_to)
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = ','.join(send_to)                                        #很重要，这里需要传入string
    msg['Date'] = formatdate(localtime = True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text,'html'))                    #设置正文内容

    with open(files,"rb") as f:
        part = MIMEApplication(f.read(),Name=basename(files))
        msg.attach(part)
        smtp = smtplib.SMTP(server,25)
        smtp.set_debuglevel(1)
        smtp.login(send_from, password)

        smtp.sendmail(send_from,send_to,msg.as_string())
        smtp.quit()

def send_report():
    send_from = "812110590@qq.com"
    send_to = ['812110590@qq.com','2225872205@qq.com','1123002509@qq.com']

    # print(type(send_to))
    # print([send_to])

    password = input('Password: ')
    
    subject = "[Automaiton]TestReport_"+str(datetime.today())
    
    files = 'F:\qgk\python\WebAutomaiton-master\WebAutomation\TestRun'+'\\'+NewModifyTime.NewFilePath()
    print('files :'+files)
    with open(files,'r') as f:
        text = f.read()

    send_email(send_from,send_to,password,subject,text,files)
