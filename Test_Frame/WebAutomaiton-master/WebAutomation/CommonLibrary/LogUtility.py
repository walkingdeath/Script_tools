import datetime
import logging
from WebAutomation.CommonLibrary import ResultFolder
# 创建一个logger对象
logger = logging.getLogger()
#设置log等级
logger.setLevel(logging.DEBUG)


def CreateLoggerFile(filename):
    try:
        # fulllogname = ResultFolder.GetRunDirectory() + "\\" + filename + ".log"
        fulllogname = 'F:\qgk\python\WebAutomaiton-master\WebAutomation\TestRun'+'\\'+filename+"{0}.log".format(datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S'))
        fh = logging.FileHandler(fulllogname)       #创建一个handler，用于写入日志文件
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s [line:%(lineno)d] %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    except Exception as err:
        logger.debug("Error when creating log file, error message: {}".format(str(err)))

def Log(message):
    logger.debug(message)